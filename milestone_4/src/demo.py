
from milestone_4.src.application import Application
from milestone_4.src.kv_store import Key
from milestone_4.src.kv_store import KeyValueStore
from milestone_4.src.dataframe import Dataframe


class Demo(Application):

    def __init__(self, idx: int, kv: KeyValueStore):
        super().__init__(idx, kv)
        self.main = Key("main", 0)
        self.verify = Key("verif", 0)
        self.check = Key("ch", 0)

    def run_(self):
        if self.this_node() == 0:
            self.producer()
        elif self.this_node() == 1:
            self.counter()
        elif self.this_node() == 2:
            self.summarizer()
        else:
            pass
    
    def producer(self):
        SZ = 100*100
        vals = [float(i) for i in range(0,SZ)]
        sum_vals = float(sum(vals))
        d = Dataframe.from_array(self.main, self.kv, SZ, vals, "F")
        s = Dataframe.from_scalar(self.check,self.kv,sum_vals, "F")

    def counter(self):
        v = self.kv.wait_and_get(self.main)
        sum_vals = sum([v.get_value(0,i) for i in range(0,100*100)])
        Dataframe.from_scalar(self.verify,self.kv,sum_vals)

    def summarizer(self):
        result = self.kv.wait_and_get(self.verify)
        expected = self.kv.wait_and_get(self.check)
        assert expected.get_value(0, 0) == result.get_value(0, 0) % "Failure"
    
if __name__ == "__main__":
    KV = KeyValueStore()    
    d = Demo(0,KV)
    d.run_()
    