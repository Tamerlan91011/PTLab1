# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class DataReader(ABC):

    @abstractmethod
    def read(self, path: str) -> any:
        pass
