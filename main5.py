# test 14
##################################################################

file = open("test.txt", "a")
if file.writable():
    ile = file.write(input("Provide text: ") + "\n")
    print("ile?:", ile)
file.close()

file = open("test.txt", "r")
if file.readable():
    print("File:")
    # for x in file:
    #     print(x)
    var1 = file.readlines()
    print(var1)
    for l in var1:
        print(l)

file.close()
