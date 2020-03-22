"""Node class that connects to primary and other nodes"""
import socket
import json


PRIMARY_ADDR = "127.0.0.2"
PRIMARY_PORT = 10000

class Node:

    def __init__(self, address, port):
        self.server_address = (address, port)
        print(f"Node started with {address} at port: {port}")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def main(self):
        """Starts the node server, for now only sends one thing"""
        self.sock.connect(self.server_address)
        msg = {"msg": "Hello from Client!"}
        self.sock.send(json.dumps(msg).encode('ascii'))
        data = self.sock.recv(1024)
        print(f"Received this: {json.loads(data)}")

if __name__ == "__main__":
    n = Node(PRIMARY_ADDR, PRIMARY_PORT)
    n.main()
