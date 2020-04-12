""" Class that serializes other classes"""

import json
from dataframe import *
from schema import *
from adapter import *

def json_helper(df):
    if "schema" in df and "data" in df:
        sc_dict = df["schema"]
        sc = Schema(sch=sc_dict["schema_list"],nrows=sc_dict["nrows"],ncols=sc_dict["ncols"])
        return Dataframe(data=df["data"],sch=sc)
    return df

def serialize_dataframe(df: Dataframe) -> str:
    df_dict = vars(df)
    df_dict['schema'] = vars(df.schema)
    return json.dumps(df_dict)

def deserialize_dataframe(str_df) -> Dataframe:
    return json.loads(str_df, object_hook=json_helper)

