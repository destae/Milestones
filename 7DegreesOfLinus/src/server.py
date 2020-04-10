import socket
import select

HEADER_LENGTH = 10


IP = "127.0.0.2"
PORT = 1234


class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((IP, PORT))
        self.server_socket.listen()
        self.sockets_list = [self.server_socket]
        self.clients = {}
        print(f'Listening for connections on {IP}:{PORT}...')

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

    def send(self, message: str):
        msg = (message["data"].decode("utf-8")).split(":")
        for client_socket in self.clients:
            if (msg[0] == "0"):
                client_socket.send(user['header'] + user['data'] + f"{len(msg[1]):<{HEADER_LENGTH}}".encode('utf-8') + msg[1].encode('utf-8'))
            else:
                if self.clients[client_socket]['data'].decode('utf-8') == msg[0]:
                    if client_socket != notified_socket:
                        client_socket.send(user['header'] + user['data'] + f"{len(msg[1]):<{HEADER_LENGTH}}".encode('utf-8') + msg[1].encode('utf-8'))


    def run(self):
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

                else:
                    message = self.receive_message(notified_socket)
                    if message is False:
                        print('Closed connection from: {}'.format(self.clients[notified_socket]['data'].decode('utf-8')))

                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]

                        continue

                    user = self.clients[notified_socket]

                    print(f'Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

                    self.send(message)
                    
            for notified_socket in exception_sockets:

                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]