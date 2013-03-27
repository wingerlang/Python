# Echo server program
import socket, sys

HOST = ''        # Symbolic name meaning all available interfaces
PORT = 1337     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print('Connected by', addr)
    data = conn.recv(1024)
    data = b'Server says' + data
    if not data:
        break
    conn.sendall(data)
conn.close()