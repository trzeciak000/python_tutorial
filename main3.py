# test 7
##################################################################

list1 = [1, 2, "a", "b", "c"]
print(list1)
print(list1[0])

text = "Hello World!"
print(text[0])

print(list1 + ["f", "g"])
print(list1 * 2)

## len() - dlugosc
print(len(list1))

i=0
while(i < len(list1)):
    print(list1[i])
    i += 1

i=0
while(i < list1.__len__()):
    print(list1[i])
    i += 1

print(list1.__len__())

list1.append("f")
print(list1)
list1.append(["g", "h"])
print(list1)
print(list1[6][0])
print(len(list1[6]))

list1.insert(2, 3)
print(list1)

## count - liczenie wystapien elementu w obiekcie
list1.append("a")
print("Ilosc:", list1.count("a"))

print("Index:", list1.index("a"))
list1.remove("a")
print(list1)
list1.remove("a")
print(list1)

list12 = [1, 5, 20, -7, 0]
print("Min:", min(list12))
print("Max:", max(list12))
list12.sort()
print(list12)
list12.reverse()
print(list12)

list12.clear()
print(list12)
list1.clear()

# test 8
##################################################################

list1 = ["Hello", "World", "Kurde"]

print(len(list1))

i = 0
while(i < len(list1)):
    print(list1[i])
    i += 1

for x in list1:
    print(x)

print(list(range(10)))

for y in range(0, 10):
    print(y)

for y in range(0, 20, 3):
    print(y)

# test 9
##################################################################

def test_function():
    print("TEST...")

test_function()

def dodaj(x):
    print(x)

dodaj(2)

def dodaj(x, y = 1):
    print(x + y)

dodaj(2, 3)
dodaj(2)

def potegowanie(x):
    return x*x

print(potegowanie(5))

var1 = potegowanie(3)
print(var1)

# test 10
##################################################################

def func(x):
    return x*x

variable = func
print(variable(5))

def func2(f1, x):
    return f1(x) * x

print(func2(func, 4))

def silnia(x):
    if(x <= 1):
        return 1
    else:
        return x * silnia(x-1)

print(silnia(5))