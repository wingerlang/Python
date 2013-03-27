# Echo client program
import socket

class Client:
    def __init__ (self):
        self.HOST = 'localhost'
        self.PORT = 1337
        self.data = None
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.s.connect((self.HOST, self.PORT))
    def receive(self, bytes = 1024):
        self.data = self.s.recv(bytes)
    def send(self, message):
        self.s.sendall(bytes(message,'UTF-8'))
    def close(self):
        self.s.close()
    def display(self):
        print("Received:", self.data)
    def __repr__(self):
        return "Socket Client" + str(self.HOST) + ':' +  str(self.PORT)

#client = Client()
#client.connect()
#client.send("This is a test")
#client.receive()
#client.display()
#client.close()