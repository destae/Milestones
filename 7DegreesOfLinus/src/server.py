import socket
import sys
import select
from queue import *
import os

HEADER_LENGTH = 10

class Server:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.ip, self.port))
        self.server_socket.listen()
        self.sockets_list = [self.server_socket]
        self.clients = {}
        print(f'Listening for connections on {self.ip}:{self.port}...')

    # Handles message receiving
    def receive_message(self, client_socket):
        try:
            message_header = client_socket.recv(HEADER_LENGTH)
            if not len(message_header):
                return False
            
            message_length = int(message_header.decode('utf-8').strip())
            return {'header': message_header, 'data': client_socket.recv(message_length)}

        except:
            return False
    
    def get_clients(self):
        return self.clients

    def send(self, message: str):
        msg = message.split("~")
        for client_socket in self.clients:
            if msg[0] == "0":
                client_socket.send(f"{len(msg[1]):<{HEADER_LENGTH}}".encode('utf-8') + msg[1].encode('utf-8'))
            else:
                if self.clients[client_socket]['data'].decode('utf-8') == msg[0]:
                    client_socket.send(f"{len(msg[1]):<{HEADER_LENGTH}}".encode('utf-8') + msg[1].encode('utf-8'))

    def run(self, shared_que: Queue):
        while True:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list)

            for notified_socket in read_sockets:

                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    user = self.receive_message(client_socket)

                    if user is False:
                        continue

                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user
                    print('Accepted new connection from {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
                    shared_que.put(('add', user['data'].decode('utf-8'), client_address[1]), block=True, timeout=None)
                    
                else:
                    message = self.receive_message(notified_socket)
                    if message is False:
                        print('Closed connection from: {}'.format(self.clients[notified_socket]['data'].decode('utf-8')))
                        shared_que.put(('remove', user['data'].decode('utf-8')), block=True, timeout=None)

                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]

                        continue

                    user = self.clients[notified_socket]

                    self.send(message["data"].decode("utf-8"))
                    
            for notified_socket in exception_sockets:

                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]


if __name__ == "__main__":
    Server()