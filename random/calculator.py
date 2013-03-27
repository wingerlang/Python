import operator

# I/0 

def getInput(display = "Enter a number: "):
    return input(display)

# String functions

def printl(str):
    print(str, end=' ')

# Math/ Number functions

def ceil(n):
    return int(n)

def top(n):
    return 0.5 + (n/1)

# Search functions

def exists(needle, stack = '+ - ^ ** '):
    return needle in stack.split()



def calculate(method, num1, num2):
    ops = {"+": operator.add, "-": operator.sub, '**': operator.pow, "^": operator.pow}

    if(exists(method)):
        return ops[method](float(num1), float(num2))
    else:
        return "Sorry, " + str(method) + " is not supported."


num1 = getInput()
method = getInput("Enter method: ")
num2 = getInput()


print(calculate(method, num1, num2))