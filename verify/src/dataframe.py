import os
import json
from verify.src import utils
from verify.src.kv_store import *
from verify.src.schema import Schema

class Dataframe:
    ## Initialises the dataframe. Creates a key value pair and inserts it into the Key Value Store
    def __init__(self, data: list, sch: Schema, key: Key=None, kv: KeyValueStore=None):
        self.schema = sch
        self.ncols = sch.get_ncols()
        self.nrows = sch.get_nrows()
        self.data = data
        if kv and key:
            kv.add_key_value(key, self.serialize_dataframe())
        
    
    #Constructor that creates a new Dataframe from an array
    @classmethod
    def from_array(cls, key: Key, kv: KeyValueStore, size: int, array: list, arr_type: str='B'):
        schem = Schema([arr_type], ncols=1, nrows=size)
        return cls([array], schem,key=key,kv=kv)
    
    #Constructor that creates a new Dataframe with a single entry: a scalar value
    @classmethod
    def from_scalar(cls, key: Key, kv: KeyValueStore, scalar: int, scalar_type: str='B'):
        schem = Schema([scalar_type], ncols=1, nrows=1)
        return cls([[scalar]], schem,key=key,kv=kv)

    ## Retrieves the number of rows of the dataframe
    def get_nrows(self):
        return self.nrows

    ## Retrives the number of columns of the dataframe
    def get_ncols(self):
        return self.ncols

    ## Gets the raw value of the data stored at the given coordinates
    def get_value(self, row: int, col: int):
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

    # Returns a string representation of this dataframe in json form.
    def serialize_dataframe(self) -> str:
        df_dict = vars(self)
        df_dict['schema'] = vars(self.schema)
        return json.dumps(df_dict)
    
    @classmethod
    def from_json(cls, str_df):
        return json.loads(str_df, object_hook=json_helper)


def json_helper(df):
    if "schema" in df and "data" in df:
        sc_dict = df["schema"]
        sc = Schema(schema_list=sc_dict["schema_list"],nrows=sc_dict["nrows"],ncols=sc_dict["ncols"])
        return Dataframe(data=df["data"],sch=sc)
    return df



def deserialize_dataframe(str_df) -> Dataframe:
    return json.loads(str_df, object_hook=json_helper)