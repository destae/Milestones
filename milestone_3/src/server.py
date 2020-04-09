import socket
import sys
import threading
import time

s = socket.socket()
s.bind(("127.0.0.1", 8080))
s.settimeout(None)
name = input(str("Please enter your username: "))
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print("Recieved connection")
print("")
s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has joined the chat room")

s.connect(("127.0.0.2", 8081))
s.send(name.encode())


def input_and_send():
   while 1:
      msg = input(str("Please enter your message: "))
      message = name+" : "+ msg
      conn.send(message.encode())
      print("Sent")
      print("")
      if msg == 'exit':
         break
   s.shutdown(socket.SHUT_RDWR)
   s.close()

background_thread = threading.Thread(target=input_and_send)
background_thread.start()

def recieve_msg():
   while 1:
      data = conn.recv(1024).decode()
      if not data:
         break
      print(s_name, ":", data)
      print("")
   conn.close()
   print("Client connection closed")


recieve_thread = threading.Thread(target=recieve_msg)
recieve_thread.start()