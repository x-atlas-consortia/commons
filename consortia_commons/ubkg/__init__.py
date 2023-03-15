from enum import IntEnum, Enum
import requests

ubkg_cache = dict()

class UbkgSuported(str, Enum):
    SENNET = 'SENNET'
    HUBMAP = 'HUBMAP'


class Ubkg:
    def __init__(self, project: UbkgSuported):
        self.project = project
        self.error = None

    def get_ubkg_valueset(self, code: str):
        try:
            self.error = None
            if code not in ubkg_cache:
                url = f"https://ontology.api.hubmapconsortium.org/valueset?parent_sab={self.project}&parent_code={code}&child_sabs={self.project}"
                response = requests.get(url)
                if response.ok:
                    ubkg_cache[code] = response.json()
        except Exception as e:
            self.error = e
            print(e)

        return ubkg_cache[code] if code in ubkg_cache else self.error

    def get_specimen_categories(self):
        return self.get_ubkg_valueset(self.specimen_categories_code)

    def get_assay_types(self):
        return self.get_ubkg_valueset(self.assay_types_code)

    def get_organ_types(self):
        return self.get_ubkg_valueset(self.organ_types_code)


def _get_sennet_codes():
    return ['C020076', 'C004000', 'C000008']


# TODO: complete
def _get_hubmap_codes():
    return []


def _get_ubkg_nodes():
    return ['specimen_categories', 'assay_types', 'organ_types']


def initialize_ubkg(project: UbkgSuported):
    try:
        ubkg_instance = Ubkg(project)
        nodes = _get_ubkg_nodes()
        codes = []
        if project is UbkgSuported.SENNET:
            codes = _get_sennet_codes()
        if project is UbkgSuported.HUBMAP:
            codes = _get_hubmap_codes()

        for i, n in enumerate(nodes):
            val = codes[i] if 0 <= i < len(codes) else None
            setattr(ubkg_instance, f"{n}_code", val)
        return ubkg_instance
    except Exception as e:
        print(e)



