""" Class that serializes other classes"""

import json
from dataframe import Dataframe
from schema import Schema



def dataframe_decoder(df):
    if "schema" in df and "data" in df:
        sc_dict = df["schema"]
        sc = Schema(sch=sc_dict["schema_list"],nrows=sc_dict["nrows"],ncols=sc_dict["ncols"])
        return Dataframe(data=df["data"],sch=sc)
    return df


def serialize_dataframe(df: Dataframe) -> str:
    df_dict = vars(df)
    df_dict['schema'] = vars(df.schema)
    print(df_dict)
    return json.dumps(df_dict)

def deserialize_dataframe(str_df) -> Dataframe:
    from dataframe import *
    return json.loads(str_df, object_hook=dataframe_decoder)



if __name__ == "__main__":
    s = Serialize()
    sc = Schema(sch=["S","S"],ncols=2,nrows=1)
    df = Dataframe(data=[["test"],["test2"]],sch=sc)
    tes = s.serialize_dataframe(df)
    print(type(tes))
    df2 = s.deserialize_dataframe(tes)
    print(df2.dataframe_to_string())