# -*- coding: utf-8 -*-
from DataReader import DataReader

import yaml

class YamlDataReader(DataReader):
    def __init__(self) -> None:
        pass

    def read(self, path: str) -> list:
        with open(path, encoding='utf-8') as file:
            data = yaml.safe_load(file)
        
        return data
