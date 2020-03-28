import socket
import sys
import threading

s = socket.socket()
s.connect((sys.argv[1], int(sys.argv[2])))
name = input(str("Please enter your username : "))
print(" Connected to chat server")
s.send(name.encode())

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