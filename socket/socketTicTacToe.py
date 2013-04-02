from socketClient import Client
from SocketServer import Server 
import sys, time, pickle, socket
tic = __import__("tictactoe2")

port, ipv4 = 1337, socket.gethostbyname(socket.gethostname())
choice = input("Type 1 for server, 2 for Client: ")

userport = input("Enter port number (default = %s): " % (port))
port = userport or port 

print("host is set to ", ipv4, "leave blank to proceed")
userhost = input("Enter the host (default = %s)" % (ipv4))
host = userhost or ipv4

print(port, host)
if choice == "1":
	game = Server(host, port)
else:
	game = Client(host, port)
game.start()

print("YOU ARE PLAYER", game.marker())

while not tic.gameover():
	tic.show()
	tic.counter += 1
	marker = tic.markers[tic.counter % 2] 
	#print("CURRENT PLAYER:", marker)

	# Determine who it is
	if game.marker() == marker:
		print("Your turn!")
		if tic.movesLeft():
			tic.place(marker)
		else:
			tic.move(marker)
		game.send(tic.board)
	else:
		print("Stay a while and listen.")
		tic.board = game.receive()

print("\nTHE GAME HAS COME TO AN END!")
tic.show()
print("WINNER: ", tic.gameover())