import socket
import select
import errno
from threading import Thread
from kv_store import *
from serialize import *
from dataframe import *


HEADER_LENGTH = 10

IP = "127.0.0.3"
PORT = 1234

class Client:
    def __init__(self, node_name: int, kv: KeyValueStore):
        self.home_node = node_name
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((IP, PORT))
        self.client_socket.setblocking(False)
        self.username = str(self.home_node).encode('utf-8')
        self.username_header = f"{len(self.username):<{HEADER_LENGTH}}".encode('utf-8')
        self.client_socket.send(self.username_header + self.username)
        self.read_thread = Thread(target=self.read)
        self.read_thread.start()
        self.store = kv
        self.tmp_dataframe = None


    def send(self, node_number: int, msg: str):
            message = str(node_number) + ":" + msg
            # If message is not empty - send it
            if message:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                print(f"{len(message):<{HEADER_LENGTH}}")
                self.client_socket.send(message_header + message)

    def read(self):
        while True:
            try:
                # Now we want to loop over received messages (there might be more than one) and print them
                while True:

                    self.username_header = self.client_socket.recv(HEADER_LENGTH)

                    if not len(self.username_header):
                        print('Connection closed by the server')
                        sys.exit()

                    username_length = int(self.username_header.decode('utf-8').strip())

                    self.username = self.client_socket.recv(username_length).decode('utf-8')

                    message_header = self.client_socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = self.client_socket.recv(message_length).decode('utf-8')
                    print("In the client")
                    print(message)
                    msg = message.split("|")
                    if (msg[0] == 'addkv'):
                        k = Key(msg[1], self.home_node)         # key
                        d = deserialize_dataframe(msg[2])       # dataframe
                        self.store.add_key_value(k, d)          # adding key value to the store

                    elif (msg[0] == 'rmkv'):
                        k = Key(msg[1], self.home_node)         # key
                        self.store.remove_key_value(k)          # removing key from store

                    elif (msg[0] == 'getkv'):
                        k = Key(msg[1], self.home_node)         # key
                        d = self.store.get_value(k)             # dataframe

                        data = "datakv|" + serialize_dataframe(d) 
                        self.send(int(msg[2]), data)

                    elif (msg[0] == "datakv"):
                        self.tmp_dataframe = deserialize_dataframe(msg[1])      # dataframe

                    print(f'{self.username} > {message}')

            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('Reading error: {}'.format(str(e)))
                    sys.exit()

                continue

            except Exception as e:
                print('Reading error: '.format(str(e)))
                sys.exit()

if __name__ == '__main__':
    n = Client(2, KeyValueStore(2))
