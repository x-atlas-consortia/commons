from atlas_consortia_commons.object import build_enum_class
from atlas_consortia_commons.ubkg import get_from_node
from atlas_consortia_commons.string import to_snake_case_upper, equals
import base64

from flask import current_app


class UbkgSDK:
    class Ops:
        as_arr = False  # Return as an array
        cb = str  # The callback function to run on value of the transform result
        as_data_dict = False  # Return as a dict
        prop_callback = to_snake_case_upper  # The callback to apply on the dict key
        data_as_val = False  # Whether to return the full UBKG data as value of key
        url_params = None  # Url parameters to apply to the request
        key = 'term'  # Which property value from the item to return as the key of the transform result
        val_key = None  # Which property value from the item to return as the value of the transform result
        obj_type = 'class'  # How to represent the return

    @staticmethod
    def ops(as_arr: bool = False, cb=str, as_data_dict: bool = False, prop_callback=to_snake_case_upper,
            data_as_val=False, url_params: str = None, key: str = 'term', val_key: str = None):
        UbkgSDK.Ops.as_arr = as_arr
        UbkgSDK.Ops.cb = cb
        UbkgSDK.Ops.as_data_dict = as_data_dict
        UbkgSDK.Ops.prop_callback = prop_callback
        UbkgSDK.Ops.data_as_val = data_as_val
        UbkgSDK.Ops.url_params = url_params
        UbkgSDK.Ops.key = key
        UbkgSDK.Ops.val_key = val_key
        return UbkgSDK

    @staticmethod
    def transform_ontology(obj, class_name: str):
        response = UbkgSDK._get_response(obj, url_params=UbkgSDK.Ops.url_params)
        obj = build_enum_class(class_name, response,
                               prop_key=UbkgSDK.Ops.key, val_key=UbkgSDK.Ops.val_key,
                               prop_callback=UbkgSDK.Ops.prop_callback,
                               obj_type=UbkgSDK._get_obj_type(UbkgSDK.Ops.as_arr, UbkgSDK.Ops.as_data_dict),
                               data_as_val=UbkgSDK.Ops.data_as_val)
        return UbkgSDK._as_list_or_class(obj, UbkgSDK.Ops.as_arr, UbkgSDK.Ops.cb)

    @staticmethod
    def entities():
        return UbkgSDK.transform_ontology(current_app.ubkg.entities, 'Entities')

    @staticmethod
    def assay_types():
        UbkgSDK.Ops.key = 'data_type'
        return UbkgSDK.transform_ontology(current_app.ubkg.assay_types, 'AssayTypes')

    @staticmethod
    def specimen_categories():
        return UbkgSDK.transform_ontology(current_app.ubkg.specimen_categories, 'SpecimenCategories')

    @staticmethod
    def organ_types():
        return UbkgSDK.transform_ontology(current_app.ubkg.organ_types, 'OrganTypes')

    @staticmethod
    def source_types():
        return UbkgSDK.transform_ontology(current_app.ubkg.source_types, 'SourceTypes')

    @staticmethod
    def node_data(obj, class_name: str = 'OntologyNode'):
        return UbkgSDK.transform_ontology(obj, class_name)

    @staticmethod
    def _as_list_or_class(obj, as_arr: bool = False, cb=str):
        return obj if not as_arr else list(map(cb, obj))

    @staticmethod
    def _get_obj_type(in_enum: bool, as_data_dict: bool = False):
        if as_data_dict:
            return 'dict'
        else:
            return 'enum' if in_enum else 'class'

    @staticmethod
    def _get_response(obj, url_params: str = None):
        endpoint = get_from_node(obj, 'endpoint')
        if type(obj) is not str and endpoint:
            if url_params is None:
                return current_app.ubkg.get_ubkg_by_endpoint(obj)
            else:
                key = base64.b64encode(url_params.encode('utf-8')).decode('utf-8')
                key = key.replace("=", '')
                return current_app.ubkg.get_ubkg(obj, key, f"{endpoint}{url_params}")
        else:
            return current_app.ubkg.get_ubkg_valueset(obj)


def init_ontology():
    UbkgSDK.specimen_categories()
    UbkgSDK.organ_types()
    UbkgSDK.entities()
    UbkgSDK.assay_types()
    UbkgSDK.source_types()