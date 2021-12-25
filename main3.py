# test 7
##################################################################

list = [1, 2, "a", "b", "c"]
print(list)
print(list[0])

text = "Hello World!"
print(text[0])

print(list + ["f", "g"])
print(list * 2)

## len() - dlugosc
print(len(list))

i=0
while(i < len(list)):
    print(list[i])
    i += 1

i=0
while(i < list.__len__()):
    print(list[i])
    i += 1

print(list.__len__())

list.append("f")
print(list)
list.append(["g", "h"])
print(list)
print(list[6][0])
print(len(list[6]))

list.insert(2, 3)
print(list)

## count - liczenie wystapien elementu w obiekcie
list.append("a")
print("Ilosc:", list.count("a"))

print("Index:", list.index("a"))
list.remove("a")
print(list)
list.remove("a")
print(list)

list2 = [1, 5, 20, -7, 0]
print("Min:", min(list2))
print("Max:", max(list2))
list2.sort()
print(list2)
list2.reverse()
print(list2)

list2.clear()
print(list2)