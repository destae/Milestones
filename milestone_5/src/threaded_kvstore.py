from kv_store import *
from adapter import *
from queue import *
from dataframe import *
import time
from threading import Thread


#A thread running node one
def node_one(shared_que: Queue):
    kv_store_1 = KeyValueStore(1)
    key_1_1 = Key("Key_1_1", 1)
    key_1_2 = Key("Key_1_2", 1)

    adpater_1 = Adapter("../data/data.sor")

    dataframe_1 = Dataframe(adpater_1.create_dataframe(0, 10), adpater_1.retrieve_schema(), key_1_1, kv_store_1)

    dataframe_2 = Dataframe(adpater_1.create_dataframe(11,20), adpater_1.retrieve_schema(), key_1_2, kv_store_1)

    while True:
        data = shared_que.get(block=True, timeout=None)
        print(kv_store_1.get_value(data).dataframe_to_string())



#A thread running node two
def node_two(shared_que: Queue):
    kv_store_2 = KeyValueStore(2)

    shared_que.put("key_1_2", block=True, timeout=None)
    time.sleep(7)
    shared_que.put("key_1_1", block=True, timeout=None)



# Main
q = Queue()
eq = Thread(target=node_one, args=(q,))
dq = Thread(target=node_two, args=(q,))

eq.start()
dq.start()
dq.join()
eq.join()
