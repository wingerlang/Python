# Echo server program
import socket, sys, pickle
class Server:
    def __init__(self, host = 'localhost', port = 1337):
        self.HOST = host
        self.PORT = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((self.HOST, self.PORT))
        self.s.listen(1)
        self.BUFFER = 1024
        self.data = "Not set"
    
    def type(self):
        return "server"

    def start(self):
        self.conn, self.addr = self.s.accept()
        #print('Connected by', self.addr)
    
    def receive(self):
        self.data = pickle.loads(self.conn.recv(self.BUFFER))
        return self.data
    def data(self, data):
        self.data = data
    def send(self, data):
        self.conn.sendall(pickle.dumps(data))
   
    def haveData(self):
        return self.data
    def marker(self):
        return "O"

    def display(self):
        print("Received:", self.data)

    def __repr__(self):
        return "Socket Server" + str(self.HOST) + ':' + str(self.PORT)
    def close(self):
        self.close()
        print("Connection closed.")

#server = Server()
#while True:
#    server.accept()
 #   server.receive()
 #   if not server.haveData():
 #       print("No data...")
 #   server.send()
#server.close()