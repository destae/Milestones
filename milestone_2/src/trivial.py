"""Trivial Example that should run for Milestone 2"""
from milestone_2.src.dataframe import Dataframe
from milestone_2.src.kv_store import KeyValueStore
from milestone_2.src.key import Key


class Trivial:
    """Will inherit from Application when applicable"""

    def __init__(self):
        self.kv = KeyValueStore()
        

    def run_(self):
        SZ = 1000*1000
        vals = [float(i) for i in range(0,SZ)]
        key = Key("triv",0)
        DF = Dataframe.from_array(key=key, KV=self.kv, size=SZ, array=vals)
        self.kv.add_key_value(key, DF)
        DF2 = self.kv.get_value(key)
        # df_sum = sum([DF.get_double(0,i) + DF2.get_double(0,i) for i in range(0,SZ)])
        # assert(df_sum == 0)
        # del DF
        # del DF2



if __name__ == "__main__":
    t = Trivial()
    t.run_()


