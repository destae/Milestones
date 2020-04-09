
import json

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


def dataframe_decoder(df):
    from dataframe import *
    from schema import *
    if "schema" in df and "data" in df:
        sc_dict = df["schema"]
        sc = Schema(sch=sc_dict["schema_list"],nrows=sc_dict["nrows"],ncols=sc_dict["ncols"])
        return Dataframe(data=df["data"],sch=sc)
    return df


def serialize_dataframe(df: Dataframe) -> str:
    from dataframe import *
    df_dict = vars(df)
    df_dict['schema'] = vars(df.schema)
    print(df_dict)
    return json.dumps(df_dict)

def deserialize_dataframe(str_df) -> Dataframe:
    from dataframe import *
    return json.loads(str_df, object_hook=dataframe_decoder)