"""Node class that connects to primary and other nodes"""
import socket
from kv_store import *
import sys


PRIMARY_ADDR = "127.0.0.2"
PRIMARY_PORT = 10000
BUFFER_SIZE = 1024

class Node:
    # Note the rendevous server should have a name = 0 because it is not part of the other client nodes
    def __init__(self, address, port, name: int, number_of_clients: int=10, rendevous: bool=False, rendevous_address=None, rendevous_port=None):
        self.name = name1
        self.server_address = (address, port)
        self.sock = self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(server_address)
        self.sock.settimeout(None)
        self.sock.listen(number_of_clients)
        self.connection_list = {} # this is a dictionary that contains address and ports key is the name
        self.rendevous_address = rendevous_address
        self.rendevous_port = rendevous_port
        self.store = KeyValueStore(self.name)

        if not rendevous:
            if self.rendevous_address == None or self.rendevous_port == None:
                print("Error: Node unable to be created because it does not know the rendevous server")
                sys.exit()
            else:
                self.sock.connect((self.rendevous_address, self.rendevous_port)) # connecting to the rendevous node
                self.connection_list.update(int(0) = [self.rendevous_address, None]) # appended the address, without a connection value, and the name = 0
   

    # Accepts connections and update the connection list of the node
    def accept_connection(self):
        conn, addr = self.sock.accept()
        name = conn.recv(BUFFER_SIZE)
        name = name.decode()
        if name == '0':
            self.connection_list.update(int(0) = [self.rendevous_address, conn]) # updates the rendevous value
        else:
            self.connection_list.update(int(name) = [addr, conn])

    # Currently takes an input encodes it and sens it to the connection of choice
    def input_and_send(self):
        while 1:
            node = input(str("Please the node you wish to send this to: "))

            if self.connection_list.get(int(node)) == None:
                print("Node value invalid")
            else:
                msg = input(str("Please enter your message: "))
                message = self.name + ": " + msg
                self.connection_list.get(int(node))[1].send(message.encode())
                if msg == 'exit':
                    self.connection_list.get(int(0))[1].send(message.encode())
                    break   
        self.sock.shutdown(socket.SHUT_RDWR)
        self.sock.close()import threading
    
    # Receives a pending message from all the nodes
    def recieve_msg(self):
        while 1:
            for k, v in self.connection_list:
                data = self.connection_list.get(k)[1].recv(BUFFER_SIZE).decode()
                if data:
                    print(data)
                    if data.contains('exit'):
                        if k == 0
                            self.sock.shutdown(socket.SHUT_RDWR)
                            self.sock.close()
                        self.connection_list.get(k)[1].close()
                        self.connection_list.pop(k)
                        print("Client connection closed")

    # Starts all the threads of the entire node
    def run(self):
        accept_thread = threading.Thread(target=self.accept_connection)
        accept_thread.start() 

        send_thread = threading.Thread(target=self.input_and_send) 
        send_thread.start()

        recieve_thread = threading.Thread(target=self.recieve_msg)
        recieve_thread.start()   

         

if __name__ == "__main__":
    n = Node(PRIMARY_ADDR, PRIMARY_PORT)
    n.main()
