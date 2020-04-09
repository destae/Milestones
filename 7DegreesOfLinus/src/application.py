"""Defines an Application Class"""
from abc import ABC, abstractmethod
from kv_store import *
from dataframe import *
from client import *
import time


class Application(ABC):
    """Abstract class"""

    def __init__(self, idx: int, kv: KeyValueStore):
        self.idx = idx
        super().__init__()
        self.node = Client(self.idx, kv)

    def get_value(self, k: Key):
        self.node.send(k.get_home(), "getkv|" + k.get_name())

        while self.node.tmp_dataframe == None:
            time.sleep(1)
        
        print((self.node.tmp_data).dataframe_to_string())           # For the time being it just prints the returned dataframe

    
    def add_value(self, k: Key, d: Dataframe):
        self.node.send(k.get_home(), "addkv|" + k.get_name() + "|" + serialize_dataframe(d))

    def remove_value(self, k: Key):
        self.node.send(k.get_home(), "rmkv|" + k.get_name())


    @abstractmethod
    def run_(self):
        pass

    def this_node(self):
        """Returns the id of this application"""
        return self.idx
