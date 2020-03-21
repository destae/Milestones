import dataframe

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

class KeyValueStore:
    def __init__(self, dataframe):
        self.dataframe_reference = dataframe
        self.row_breakout: int = 0 # this indicates the number of rows each key recieves, it is something that can be recalculated 
        self.key_store: list  = [] # empty during initialisation -- the max size it can be is the number of rows from the dataframe that this key store contains
