# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and set/tings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# test 1
#################################################################
print(5+5)

var1 = "Hi"
# var2 = input("write something: ")
#
# print(var1 + " " + var2)

# test 2
##################################################################

print("kolejnosc: ")
print(2+2*2)
print((2+2)*2)
print("Dzielenie:")
print(5/2)
print(5//2)
print("Potegowanie:")
print(2**4)

print("konwersja:")
# a = int(input("podaj 1: "))
# b = int(input("podaj 2: "))
# print(a+b)
# del a

# test 3
##################################################################

print(5>6)
a = 5
b = 5
if a == b:
    print("True")

a=15
b=10

if a > b:
    print("More")
elif a == b:
    print("Equal")
else:
    print("Less")
print("End")

# test 4
##################################################################
wiek = 19
kasa = 40

if wiek < 12 or (wiek >= 12 and kasa >= 35):
    print("ok")
else:
    print("not ok")

if not wiek > 12 or (wiek >= 12 and kasa >= 35):
    print("ok")
else:
    print("not ok")

if (True or False) and not False:
    print("True")
else:
    print("False")

# test 5
##################################################################

i = 0

while(i < 10):
    i += 1
    print(i)

i = 0

while(1):
    i += 1
    if i % 2 == 1:
        continue
    print(i)
    if i >= 10:
        break

