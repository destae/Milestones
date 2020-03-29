from kv_store import *
from adapter import *
from queue import *

#A thread running node one
def node_one(shared_que: Queue):
    kv_store_1 = KeyValueStore(1)
    
    adpater_1 = Adapter("")
    dataframe_1 = adpater_1.retrieve_dataframe()

    adpater_2 = Adapter("")
    dataframe_2 = adapter_2.retrieve_dataframe()

    key_1_1 = Key("Key_1_1", 1)
    key_1_2 = Key("Key_1_2", 1)


    while True:
        shared_que.get(block=True, timeout=False, daemon)

