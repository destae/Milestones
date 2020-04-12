
import sys
from verify.src.application import Application
from verify.src.kv_store import Key
from verify.src.kv_store import KeyValueStore
from verify.src.dataframe import Dataframe
from verify.src.server import Server


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
        del d
        del s

    def counter(self):
        v = Dataframe.from_json(self.kv.wait_and_get(self.main))
        sum_vals = sum([v.get_value(0,i) for i in range(0,100*100)])
        Dataframe.from_scalar(self.verify,self.kv,sum_vals)

    def summarizer(self):
        result = Dataframe.from_json(self.kv.wait_and_get(self.verify))
        expected = Dataframe.from_json(self.kv.wait_and_get(self.check))
        assert expected.get_value(0, 0) == result.get_value(0, 0) % "Failure"
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    else:
        node_id = int(sys.argv[1])
        S = Server()
        KV = KeyValueStore(node_id)    
        d = Demo(node_id,KV)
        d.run_()
    