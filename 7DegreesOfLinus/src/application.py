"""Defines an Application Class"""
from kv_store import *
from dataframe import *
from client import *
import time
from queue import *


class Application():
    def __init__(self, ip: str, port: int, idx: int, shared_que: Queue):
        self.main = Key("main", 1)
        self.check = Key("ch", 1)
        self.verify = Key("verif", 1)

        self.idx = idx
        self.app_que = Queue()
        self.node = Client(ip, port, self.idx, shared_que, self.app_que)

    '''
    Gets the value of the key stored somewhere on the network.
    '''
    def get_value(self, k: Key):
        self.node.send(k.get_home(), "getkv|" + str(k.get_name()) + "|" + str(self.idx))
        data = self.app_que.get(block=True, timeout=None)
        
        return data[1] # returning the dataframe
    
    '''
    Application run determines the node that it is and runs the appropriate function that corresponds with it.
    '''
    def run(self):
        if self.this_node() == 1:
            self.producer()
        elif self.this_node() == 2:
            self.counter()
        elif self.this_node() == 3:
            self.summarizer()
        else:
            pass
    
    '''
    Produces two key value pairs to be stored in the first node.
    '''
    def producer(self):
        SZ = 100*10
        vals = [float(i) for i in range(0,SZ)]
        sum_vals = float(sum(vals))

        tmp_schm1 = Schema([utils.schema_from_list(vals)], 1, len(vals))
        tmp_data1 = Dataframe([vals], tmp_schm1) 
        self.add_value(self.main, tmp_data1)
         
        tmp_schm2 = Schema([utils.determine_type(str(sum_vals))], 1, 1)
        tmp_data2 = Dataframe([[sum_vals]], tmp_schm2)
        self.add_value(self.check, tmp_data2)

        print("Completed producer")

    '''
    Counter function.
    Retrieves the stored key from the 1st node and sums the value contained within it.
    '''
    def counter(self):
        v = self.get_value(self.main)
        v_data = v.get_data()

        sum_vals = sum([v_data[0][i] for i in range(0, 100*10)])
        tmp_schm2 = Schema([utils.determine_type(str(sum_vals))], 1, 1)
        tmp_data2 = Dataframe([[sum_vals]], tmp_schm2)
        self.add_value(self.verify, tmp_data2)
        print("Completed counter")

    '''
    Determines if the result and the expected values are the same. 
    Prints to console with result and asserts the reply.
    '''
    def summarizer(self):
        result = self.get_value(self.verify)
        expected = self.get_value(self.check)
        
        summary = (expected.get_value(0, 0) == result.get_value(0, 0))
        print("Summarizer: " + str(summary))
        assert summary  % "Failure"
    
    def add_value(self, k: Key, d: Dataframe):
        self.node.send(k.get_home(), "addkv|" + k.get_name() + "|" + serialize_dataframe(d))

    def remove_value(self, k: Key):
        self.node.send(k.get_home(), "rmkv|" + k.get_name())

    def retrieve_value(self, k: Key):
        return self.node.retrieve_value(k)
    
    def this_node(self):
        """Returns the id of this application"""
        return self.idx
