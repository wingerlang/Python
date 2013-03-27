# I/0 

def getInput(display = "Enter a number: "):
    return input(display)

# String functions

def printl(str):
    print(str, end=' ')

# Math/ Number functions

def ceil(n):
    return int(n)

def round(n):
    return int(0.5 + n)

def top(n):
    return int(0.999 + n)

# Search functions
def exists(needle, stack = '+ - ^ ** '):
  return needle in stack.split()
def substr(sub, stri):
    return sub in stri
def substri(sub, stri):
    return sub.lower() in stri.lower()