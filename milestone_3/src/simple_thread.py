from queue import Queue
from threading import Thread
from random import shuffle

# A thread that reads in a command line input and adds to the queue that it takes in
def enq(out_q: Queue):
    for a in range(7):
        x = "sequence"
        l = list(x)
        shuffle(l)
        y = ''.join(l)
        out_q.put(y, block=True, timeout=None)


# A thread that pops out the data from the queue and prints it out
def deq(in_q: Queue):
    for x in range(7):
        data = in_q.get(block=True, timeout=None)
        print("Dequeue: " + str(data))


# Main
q = Queue()
eq = Thread(target=enq, args=(q,))
dq = Thread(target=deq, args=(q,))
eq.start()
dq.start()
eq.join()
dq.join()
