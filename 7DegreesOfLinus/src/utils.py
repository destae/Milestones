
import json
from dataframe import Dataframe
from schema import Schema

## Determines the type of a single data point
def determine_type_with_index(data, start_index, end_index):

    if start_index == end_index or end_index < start_index:
        return 'B'

    temp_data = remove_whitespace(data[start_index:end_index])
    return determine_type(temp_data)

def determine_type(data):
    if any(c.isalpha() for c in data):
        return 'S'

    elif "\"" in data:
        return 'S'

    elif "." in data:
        return 'F'

    elif "-" in data:
        return 'I'

    elif data == "1" or data == "0":
        return 'B'

    elif not(any(c.isalnum() for c in data)):
        return 'B'

    else:
        return 'I'


## Removes the whitespace of a given data point
def remove_whitespace(data):
    return data.strip()

## Changes a string to a lsit
def string_to_list(data):
    return eval(data)



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
  return json.loads(str_df, object_hook=dataframe_decoder)