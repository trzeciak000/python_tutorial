# test 15
##################################################################

dictionary = {1: "monday", 2: "tuesday", 7: "sunday"}

print(dictionary[2])
print(dictionary[7])
dictionary[3] = "wednesday"
print(dictionary)
dictionary[8] = False
dictionary["saturday"] = 6
print(dictionary)

print(dictionary.get(9, "index not found"))

for l in dictionary.values():
    print(l)

for l in dictionary.keys():
    print(dictionary[l])

print(dictionary.pop(1))
print(dictionary)

# test 16
##################################################################

krotka = (2, 4, 8, 16, 32, 64)
print(krotka[0])
print(krotka[4])
print(krotka)
#krotka[0] = 1

print("Elements:", krotka.count(64))
print("Index:", krotka.index(32))

print(krotka[0:3])
print(krotka[3:5])
print(krotka[0:100])
print(krotka[-4:-2])
print(krotka[0::2])
print(krotka[::-1])