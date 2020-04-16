""" Class that serializes other classes"""

import json
from dataframe import *
from schema import *

'''
Assists in the reconstruction of a dataframe object.
It builds up the indvidual aspects of the dataframe.
'''
def json_helper(df):
    if "schema" in df and "data" in df:
        sc_dict = df["schema"]
        sc = Schema(sch=sc_dict["schema_list"],nrows=sc_dict["nrows"],ncols=sc_dict["ncols"])
        d = Dataframe(data=df["data"],sch=sc)
        return d
    return df

'''
Serialises the dataframe into a string object. It constructs a JSON.
'''
def serialize_dataframe(df: Dataframe) -> str:
    df_dict = vars(df)
    tmp_dict = df_dict.copy()
    tmp_dict['schema'] = vars(df.schema)
    return json.dumps(tmp_dict)

'''
Deconstructs a dataframe from a string.
'''
def deserialize_dataframe(str_df) -> Dataframe:
    return json.loads(str_df, object_hook=json_helper)

