from milestone_3.src import utils
import os
from milestone_3.src.kv_store import Key
from milestone_3.src.kv_store import KeyValueStore
from milestone_3.src.schema import Schema

class Dataframe:
    def __init__(self, data: list, sch: Schema):
        self.schema = sch
        self.ncols = sch.get_ncols()
        self.nrows = sch.get_nrows()
        self.data = data
    
    ## Retrieves the number of rows of the dataframe
    def get_nrows(self):
        return self.nrows

    ## Retrives the number of columns of the dataframe
    def get_ncols(self):
        return self.ncols

    ## Gets the raw value of the data stored at the given coordinates
    def get_value(self, col: int, row: int):
        if (col < self.get_ncols() and col >= 0 and row >= 0 and row < self.get_nrows()):
            return self.data[row][col]

    ## Returns the type of of the value stored at the given coordinates
    def get_type(self, col: int, row: int):
        if (col < self.get_ncols() and col >= 0 and row >= 0 and row < self.get_nrows()):
            return self.schema.get_schema()[col]

    ## Constructs a string from the dataframe
    def dataframe_to_string(self):
        tmp_string = ""
        for row in self.data:
            tmp_string += str(row) + "\n"
        print(tmp_string)
        return tmp_string

    @classmethod
    def from_array(cls, key: Key, kv: KeyValueStore, size: int, array: list, arr_type: str='B'):
        schem = Schema([arr_type], ncols=1, nrows=size)
        return cls(array, schem)
    
    @classmethod
    def from_scalar(cls, key: Key, kv: KeyValueStore, scalar: int, scalar_type: str='B'):
        pass