from enum import Enum
import requests
from consortia_commons.file import load_config_by_key
import json

ubkg_cache = dict()
config_key = 'UBKG'

class Ubkg:
    def __init__(self):
        self.error = None

    def get_ubkg_valueset(self, code: str):
        try:
            self.error = None
            if code not in ubkg_cache:
                server = load_config_by_key(config_key, 'server')
                server_pathname = load_config_by_key(config_key, 'server_pathname')
                url = f"{server}{server_pathname}"
                url = url.format(code=code)
                response = requests.get(url)
                if response.ok:
                    ubkg_cache[code] = response.json()
        except Exception as e:
            self.error = e
            print(e)

        return ubkg_cache[code] if code in ubkg_cache else self.error


def initialize_ubkg():
    try:
        ubkg_instance = Ubkg()
        codes_str = load_config_by_key(config_key, 'codes')
        codes = json.loads(codes_str)
        for node, code in codes.items():
            setattr(ubkg_instance, f"{node}", code)
        return ubkg_instance
    except Exception as e:
        print(e)



