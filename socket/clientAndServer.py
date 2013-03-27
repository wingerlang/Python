from socketClient import Client
from SocketServer import Server 




try:
	game = Client()
	game.connect()
except:
	game = Server()
	game.accept()

print(game)