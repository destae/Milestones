"""Defines an Application Class"""
from kv_store import *
from dataframe import *
from client import *
import time
from queue import *


class Application():
    def __init__(self, idx: int, shared_que: Queue):
        self.idx = idx
        self.node = Client(self.idx, shared_que)

    def get_value(self, k: Key):
        self.node.send(k.get_home(), "getkv|" + str(k.get_name()) + "|" + str(self.idx))
        print("Sent to node")
        
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

    def retrieve_value(self, k: Key):
        return self.node.retrieve_value(k)
    
    def this_node(self):
        """Returns the id of this application"""
        return self.idx

if __name__ == "__main__": 
    Application(2)