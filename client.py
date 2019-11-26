import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 221))
s.send("Who are you?".encode())
data = s.recv(1024)
s.close()
data = data.decode()
print ("Received", data)