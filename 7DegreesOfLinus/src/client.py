import socket
import select
import errno
from threading import Thread
from kv_store import *
from serialize import *
from dataframe import *
import sys
from queue import *

HEADER_LENGTH = 10

IP = "127.0.0.4"
PORT = 1234

class Client:
    '''
    Initialises the client object.
    '''
    def __init__(self, node_name: int, shared_queue: Queue):
        self.home_node = node_name
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)
        self.username = str(self.home_node).encode('utf-8')
        self.username_header = f"{len(self.username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(self.username_header + self.username)
        
        self.read_thread = Thread(target=self.read, args=(shared_queue,))
        self.read_thread.start()
        
        self.store = KeyValueStore(node_name)
        self.tmp_dataframe = None

    def retrieve_value(self, k: Key):
        return self.store.get_value(k)
    '''
    Sends a message to the specified node.
    '''
    def send(self, node_number: int, msg: str):
            message = str(node_number) + "~" + msg
            # If message is not empty - send it
            if message:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                print(f"{len(message):<{HEADER_LENGTH}}")
                self.client_socket.send(message_header + message)

    '''
    Reads the incoming message or throws an exception.
    Updates the key value store that is associated with the node.
    '''
    def read(self, shared_queue: Queue):
        while True:
            try:
                message_header = self.client_socket.recv(HEADER_LENGTH)
                if not len(message_header):
                    print('Connection closed by the server')
                    sys.exit()

                message_length = int(message_header.decode('utf-8').strip())
                print(message_length)
                message = self.client_socket.recv(message_length).decode('utf-8')
                print("In the client")
                msg = message.split("|")
                print(msg)
                if (msg[0] == 'addkv'):
                    k = Key(msg[1], self.home_node)         # key
                    d = deserialize_dataframe(msg[2])       # dataframe
                    self.store.add_key_value(k, d)          # adding key value to the store

                    dd = self.store.get_value(k)

                    shared_queue.put(('add', k.get_name()), block=True, timeout=None)

                elif (msg[0] == 'rmkv'):
                    k = Key(msg[1], self.home_node)         # key
                    self.store.remove_key_value(k)          # removing key from store

                    shared_queue.put(('remove', k.get_name()), block=True, timeout=None)

                elif (msg[0] == 'getkv'):
                    k = Key(msg[1], self.home_node)         # key
                    d = self.store.get_value(k)             # dataframe

                    data = "datakv|" + str(self.home_node) + "|" + str(msg[1]) + "|" + serialize_dataframe(d) 
                    self.send(int(msg[2]), data)

                elif (msg[0] == "datakv"):
                    k = Key(str(msg[2]), int(msg[1]))
                    d = deserialize_dataframe(str(msg[3]))
                    self.shared_que.put(('retrieve', k, d), block=True, timeout=None)

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()

                continue

            except Exception as e:
                print('Reading error: '.format(str(e)))
                sys.exit()

if __name__ == "__main__":
    q = Queue()
    Client(3, q)