import os
import configparser


def load_config():
    config = configparser.ConfigParser()
    try:
        config.read(os.path.join(os.path.dirname(__file__), '..', 'app.properties'))
    except Exception as e:
        print(e)
    return config


def load_config_by_key(section_key: str, prop_key: str):
    config = load_config()
    try:
        return config.get(section_key, prop_key)
    except Exception as e:
        print(e)


def load_config_by_keys(section_key: str, prop_keys: list):
    result = {}
    try:
        for p in prop_keys:
            result[p] = load_config_by_key(section_key, p)
    except Exception as e:
        print(e)
    return result
