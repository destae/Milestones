"""Defines an Application Class"""
from kv_store import *
from dataframe import *
from client import *
import time


class Application():
    def __init__(self, idx: int):
        self.shared_queue = Queue()
        self.idx = idx
        self.node = Client(self.idx, self.shared_queue)

    def get_value(self, k: Key):
        self.node.send(k.get_home(), "getkv|" + k.get_name())

        while self.node.tmp_dataframe == None:
            time.sleep(1)
        
        print((self.node.tmp_data).dataframe_to_string())           # For the time being it just prints the returned dataframe

    def run_(self):
        if self.this_node() == 1:
            self.producer()
        elif self.this_node() == 2:
            self.counter()
        elif self.this_node() == 3:
            self.summarizer()
        else:
            pass
    
    def add_value(self, k: Key, d: Dataframe):
        self.node.send(k.get_home(), "addkv|" + k.get_name() + "|" + serialize_dataframe(d))

    def remove_value(self, k: Key):
        self.node.send(k.get_home(), "rmkv|" + k.get_name())
    
    def get_value(self, k: Key):
        self.node.send(k.get_home(), "getkv|" + k.get_name() + "|" + str(self.idx))

    def this_node(self):
        """Returns the id of this application"""
        return self.idx
