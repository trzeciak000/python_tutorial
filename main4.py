# test 11
##################################################################

import random
from math import pi
from math import sqrt as pierwiastek

print(random.randint(5, 9))
print(pi)
print(pierwiastek(25))

# test 12
##################################################################

x = 12
y = 0

#print(x / y)

try:
    print(x + "!")
    print(x / y)
    print("line after")
except ZeroDivisionError:
    print("dividing by 0")
except TypeError:
    print("unsupported types for +")

print("OK!")

try:
    lista = []
    print(lista[0])
    print(x + "!")
    print(x / y)
    print("line after")
except (ZeroDivisionError, TypeError):
    print("1 of 2 exceptions")
except:
    print("OTHER EXCEPTION")
finally:
    print("FINAL INSTRUCTION!")

print("ok")

# test 13
##################################################################

def dzielenie(x, y):
    assert y != 0, "Y == 0"
    if y == 0:
        raise ZeroDivisionError("Dividing by 0")
    print(x / y)

try:
    dzielenie(5, 1)
except ZeroDivisionError:
    print("Error!")
    raise