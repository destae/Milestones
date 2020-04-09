import socket
import sys
import threading

s = socket.socket()
port = 8081
host = "127.0.0.2"
s.bind((host,port))
s.settimeout(None)

s.connect(("127.0.0.1", 8080))
name = input(str("Please enter your username : "))
print(" Connected to chat server")
s.send(name.encode())

s.listen(1)
conn, addr = s.accept()
print("Recieved connection")
print("")

def receive_and_print():
    for msg in iter(lambda: s.recv(1024).decode(), ''):
        print(":", msg)
        print("")
        

        
background_thread = threading.Thread(target=receive_and_print, daemon=True)
background_thread.start()

while 1:
    s.send(input("Please enter your message: ").encode())
    print("Sent")
    print("")