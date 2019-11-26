import socket
import random 

def Main():
    host = "127.0.0.1"
    port = 221
     
    mySocket = socket.socket()
    mySocket.bind((host,port))
     
    mySocket.listen(1)
    print ("Listening...")
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print ("from connected  user: " + str(data))
             
            randNum = random.randint(1,3)
            if randNum == 1:
                conn.send("Yes".encode())
            if randNum == 2:
                conn.send("No".encode())
            if randNum == 3:
                conn.send("Maybe so".encode())
            print ("sending answer")
             
    conn.close()
     
if __name__ == '__main__':
    Main()