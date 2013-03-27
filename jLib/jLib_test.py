import unittest

f = __import__("jLib")

# The basic idea of unit testing.


units, i = [], 0

units.append(f.top(5.9) == 6)

units.append(f.top(5.1) == 6)
units.append(f.ceil(5.0) == 5)
units.append(f.ceil(5.9) == 5)
units.append(f.substr("A", "ABCDEF"))
units.append(False == f.substr("a", "BCDAEF"))
units.append(True == f.substri("a", "BCDAEF"))


print(units)
testNr = 1
for result in units:
    print(str(testNr) + ': ' + str(result))
    testNr += 1