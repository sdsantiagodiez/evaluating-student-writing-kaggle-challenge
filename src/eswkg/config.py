#YAML configuration gathering
import yaml
import logging
from pathlib import Path


class Config:
    _repository_file_path = Path(__file__).parents[2]
    _catalog_file_path = _repository_file_path / "conf/base/catalog.yml"

    def __init__(self,repository_file_path):
        self._repository_file_path = repository_file_path

    @staticmethod
    def _get_dictionary_key_value(dictionary, key):
        try:
            if key not in dictionary:
                raise Exception(f"Key {key} not found in configuration file")
        except Exception as e:
            logging.exception(str(e))
            return None
        else:
            return dictionary[key]
    
    @staticmethod
    def _get_catalog_config(catalog_file_path=_catalog_file_path):
        try:
            with open(catalog_file_path, "r") as stream:
                catalog = yaml.safe_load(stream)
        except yaml.YAMLError as e:
            logging.exception(str(e))
        except Exception as e:
            logging.exception(str(e))
        else:
            return catalog
    
    @staticmethod
    def get_config(config_key, catalog_file_path=_catalog_file_path):
        catalog_config = Config._get_catalog_config(catalog_file_path)
        return Config._get_dictionary_key_value(catalog_config, config_key)
        
    @staticmethod
    def get_file_path(config_key, catalog_file_path=_catalog_file_path):
        file_path_key = "filepath"
        config = Config.get_config(config_key,catalog_file_path)
        return Config._get_dictionary_key_value(config,file_path_key)

    
        