
from milestone_3.src.application import Application
from milestone_3.src.kv_store import Key
from milestone_3.src.kv_store import KeyValueStore
from milestone_3.src.dataframe import Dataframe


class Demo(Application):


    def __init__(self, idx):
        super().__init__(idx)
        self.main = Key("main", 0)
        self.verify = Key("verif", 0)
        self.check = Key("ch",0)

    def run_(self):
        if self.this_node() == 0:
            self.producer()
        elif self.this_node() == 1:
            self.counter()
        elif self.this_node() == 2:
            self.summarizer()
        else:
            pass
    

#   void producer() {
#     size_t SZ = 100*1000;
#     double* vals = new double[SZ];
#     double sum = 0;
#     for (size_t i = 0; i < SZ; ++i) sum += vals[i] = i;
#     DataFrame::fromArray(&main, &kv, SZ, vals);
#     DataFrame::fromScalar(&check, &kv, sum);
#   }
 

    def producer(self):
        SZ = 100*100
        vals = [float(i) for i in range(0,SZ)]
        sum = float(sum(vals))
        DF = Dataframe.fromArray(self.main, )
        DF = Dataframe.fromScalar(self.check)

    def counter(self):
        pass
    

    def summarizer(self):
        pass
    
#   void counter() {
#     DataFrame* v = kv.waitAndGet(main);
#     size_t sum = 0;
#     for (size_t i = 0; i < 100*1000; ++i) sum += v->get_double(0,i);
#     p("The sum is  ").pln(sum);
#     DataFrame::fromScalar(&verify, &kv, sum);
#   }
 
#   void summarizer() {
#     DataFrame* result = kv.waitAndGet(verify);
#     DataFrame* expected = kv.waitAndGet(check);
#     pln(expected->get_double(0,0)==result->get_double(0,0) ? "SUCCESS":"FAILURE");
#   }
# };