import enum
from typing import Union
from consortia_commons.string import to_pascal_case


def build_enum_class(class_name: str, data: Union[list, dict], key: str = None, val_callback=None):
    _enums = {}
    try:
        if type(data) is list:
            for item in data:
                val = item.get(key)
                _enums[to_pascal_case(val)] = val if val_callback is None else val_callback(val)
        else:
            if key is not None:
                val = data.get(key)
                _enums[to_pascal_case(val)] = val if val_callback is None else val_callback(val)
            else:
                _enums = data
        return enum.Enum(class_name, _enums)
    except Exception as e:
        print(e)
