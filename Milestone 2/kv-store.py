from dataframe import Dataframe

class Key:
    def __init__(self, name: str, home: int):
        self.name = name
        self.home = home

    def set_home(self, home: int):
        self.home = home
    
    def get_home(self):
        return self.home

    def set_name(self, name: str):
        self.name = name

    def get_name(self):
        return self.name

class KeyValue:
    def __init__(self, key: Key, value):
        self.key = key
        self.value = value
        self.ncols_breakout = 0
    
    def get_key(self):
        return self.key

    def set_key(self, key: Key):
        self.key = key

    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def get_home_node(self):
        return self.key.get_home()
    
    def set_ncols_breakout(self, breakout: int):
        self.ncols_breakout = breakout

class KeyValueStore:
    def __init__(self, data: Dataframe):
        self.dataframe_reference = data
        self.key_store: list  = [] # empty during initialisation -- the max size it can be is the number of columns from the dataframe that this key store contains

    def add_key_value(self, keyvalue: KeyValue):
        self.key_store.append(keyvalue)

    def calculate_breakout(self, array_size: int, ncols: int):
        if array_size % ncols != 0:
            tmp_val = array_size % ncols
        else: 
            for elem in self.key_store:
                elem.set_ncols_breakout(array_size/ncols)
            