import time

def show():
    print("\nCurrent Board:\n---------------------")
    for slot in range(1, len(board)):
        print(board[slot], end = ' ')
        if slot and slot % 3 == 0:
            print()

def place(marker):
    """
    choice = len(board)
    while True:
        if choice < len(board) and board[choice] not in markers:
            board[choice] = marker
            break;
        else:
            choice = int(input(marker + " select a spot: "))
    """
    choice = -1
    while True:
        try:
            if type(choice) == int and choice > 0 and choice < len(board) and board[choice] not in markers:
                board[choice] = marker
                break
            else:
                choice = int(input(marker + " select a spot: "))
        except:
            pass


def move(marker):
    try:
        userFrom = int(input("\n" + marker + " move your marker from: "))
        userTo = int(input("Move your marker To: "))
    except:
        userFrom, userTo = -1, -1

    if userFrom > 0  and userFrom < len(board):
        if board[userFrom] == marker and board[userTo] not in markers:
            board[userTo] = marker
            board[userFrom] = userFrom
        else:
            print("Please make a valid move next turn.")
    else:
        print("PLease enter a number between 0 and 9 nexr turn.")

def movesLeft(marker):
    return board.count(marker) < 3

def row(marker):
    f = board[1:4].count(marker)
    s = board[4:7].count(marker)
    t = board[7:10].count(marker)
    return True if ((f == 3) or (s == 3) or (t == 3)) else False

def col(marker):
    f = board[1::3].count(marker)
    s = board[2::3].count(marker)
    t = board[3::3].count(marker)
    return True if ((f == 3) or (s == 3) or (t == 3)) else False

def diag(marker):
    right = board[1::4].count(marker)
    left = board[3:-2:2].count(marker)
    return (right == 3) or (left == 3) or False

def gameover():
    for mark in markers:
        r, c, d = row(mark), col(mark), diag(mark)
        if any([r, c, d]):
            return mark
    return False

board = ['', 1, 2, 3, 4, 5, 6, 7, 8, 9]
markers, counter = ['X', 'O'], 0

"""
while not gameover():
    counter += 1
    marker = markers[counter % 2] 
    show()
    if movesLeft():
        place(marker)
    else:
        move(marker)
print("WINNER: ", gameover())
"""