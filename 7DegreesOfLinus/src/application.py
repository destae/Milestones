"""Defines an Application Class"""
from abc import ABC, abstractmethod
from kv_store import *



class Application(ABC):
    """Abstract class"""

    def __init__(self, idx: int, kv: KeyValueStore):
        self.idx = idx
        self.kv = kv
        super().__init__()

    @abstractmethod
    def run_(self):
        pass

    def this_node(self):
        """Returns the id of this application"""
        return self.idx

    def request_key(self, k: Key):
        self.kv.get_value(k)