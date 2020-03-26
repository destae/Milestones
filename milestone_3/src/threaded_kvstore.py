from kv_store import *
from adapter import *

#A thread running node one
def node_one():
    kv_store_1 = KeyValueStore()
    kv_store_1.update_home_node(1)

    adpater_1 = Adapter("")
    dataframe_1 = adpater_1.retrieve_dataframe()

    adpater_2 = Adapter("")
    dataframe_2 = adapter_2.retrieve_dataframe()

    key_1_1 = Key("Key_1_1", 1)
    key_1_2 = Key("Key_1_2", 1)

    kv_store_1.add_key_value(key_1_1, dataframe_1)
    kv_store_1.add_key_value(key_1_2, dataframe_2)

