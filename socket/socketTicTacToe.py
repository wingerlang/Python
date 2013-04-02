from socketClient import Client
from SocketServer import Server 
import sys, time, pickle

tic = __import__("tictactoe2")

#choice = input("Type 1 for server, 2 for Client: ")
choice = input("Type 1 for server, 2 for Client: ")
#host = input("Enter the host (Example: localhost)")
#port = input("Enter port (example 1337")
host = 'localhost'
port = 1337
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


print()
tic.show()
print("WINNER: ", tic.gameover())