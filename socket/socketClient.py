# Echo client program
import socket, pickle

class Client:
    def __init__ (self, host = 'localhost', port = 1337):
        self.HOST = host
        self.PORT = port
        self.data = None
        self.BUFFER = 1024
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def start(self):
        self.s.connect((self.HOST, self.PORT))

    def receive(self):
        self.data = pickle.loads(self.s.recv(self.BUFFER))
        return self.data
    def send(self, data):
        self.s.sendall(pickle.dumps(data))
    
    def data(self, data):
        self.data = data
    def marker(self):
        return "X"
    def type(self):
        return "client"
    def display(self):
        print("Received:", self.data)
    def __repr__(self):
        return "Socket Client" + str(self.HOST) + ':' +  str(self.PORT)
    def close(self):
        self.s.close()
        print("Connection closed.")

#client = Client()
#client.connect()
#client.send("This is a test")
#client.receive()
#client.display()
#client.close()