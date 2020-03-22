""" Rendevouz server"""
import socket
import select
import json
from queue import Queue
from queue import Empty

class Primary:
    """Rendevouz server that receives node information and sends it to every node that
    successfully connects
    Inspired from: https://steelkiwi.com/blog/working-tcp-sockets/"""

    def __init__(self, server_name, port):

        self.server_address = (server_name, port)
        print(f"Primary server: {server_name}, at port: {port}")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.inputs = [self.sock]
        self.outputs = []
        self.message_queues = {}


    def handle_socket(self, sock):
        """handle the sockets in self.readable"""
        if sock is self.sock:
            connection, client_address = sock.accept()
            connection.setblocking(0)
            self.inputs.append(connection)
            self.message_queues[connection] = Queue()
        else:
            data = sock.recv(1024)
            if data:
                d = json.loads(data)
                print(f"Received this data: {d}")
                self.message_queues[sock].put(data)
                if sock not in self.outputs:
                    self.outputs.append(sock)
            else:
                if sock in self.outputs:
                    self.outputs.remove(sock)
                self.inputs.remove(sock)
                sock.close()
                del self.message_queues[sock]

    def send_next_msg(self, sock):
        """ Sends the next message in the message_queue"""
        try:
            next_msg = self.message_queues[sock].get_nowait()
        except Empty:
            self.outputs.remove(sock)
        else:
            sock.send(next_msg)

    def handle_exceptions(self, sock):
        """ Removes any sock from all lists that has trouble"""
        self.inputs.remove(sock)
        if sock in self.outputs:
            self.outputs.remove(sock)
        sock.close()
        del self.message_queues[sock]

    def main(self):
        """Starts the rendevouz server"""
        self.sock.setblocking(0)
        self.sock.bind(self.server_address)
        self.sock.listen(5)

        while(self.inputs):
            readable, writable, exceptions = select.select(self.inputs, self.outputs, self.inputs)
            for s in readable:
                self.handle_socket(s)
            for s in writable:
                self.send_next_msg(s)
            for s in exceptions:
                self.handle_exceptions(s)



if __name__ == "__main__":
    LOCALHOST = '127.0.0.2'
    PORT = 10000
    P = Primary(LOCALHOST,PORT)
    P.main()
