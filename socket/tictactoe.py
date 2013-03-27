import time

def getMove(f):
	printcoord()
	pos = input("Make your move (yx): ")
	try:
		y, x = int(pos[0]), int(pos[1])
		if y < len(f) and x < len(f[y]):
			print(pos[0],pos[1])
	except:
		print("ERROR")
	return pos

def valid_move(f,move):
	return True

def printcoord(h = 3, w = 3):
	for y in range(h):
		print('[', end = ' ')
		for x in range(w):
			print(str(y)+str(x), end = ' ')
		print(']')

def printField(f):
	for y in range(len(f)):
		print('[', end = ' ')
		for x in range(len(f[y])):
			print(f[y][x], end = ' ')
		print(']')

def movesLeft(f):
	moves = 0
	for row in range(len(f)):
		moves += f[row].count(' ')
	return moves

field = [
	[' ',' ',' '],
	[' ',' ',' '],
	[' ',' ',' ']]
m1, m2 = 'X', 'O'

getMove(field)