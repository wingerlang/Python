# Echo server program
import socket, sys
class Server:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 1337
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(1)
        self.BUFFER = 1024
        
    def accept(self):
        self.conn, self.addr = self.s.accept()
        print('Connected by', self.addr)
    
    def recieve(self):
        self.data = self.conn.recv(self.BUFFER)
   
    def send(self):
        self.conn.sendall(self.data)
    
    def close(self):
        self.close()
        print("Connection closed.")
    def haveData(self):
        return self.data

server = Server()
while True:
    server.accept()
    server.recieve()
    if not server.haveData():
        print("No data...")
    server.send()
server.close()