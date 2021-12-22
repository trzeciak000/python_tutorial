# test 6
##################################################################

from random import randint

random = randint(1, 10)

i = 0
while (1):
    i += 1
    a = int(input("Guess numeber 1-10: "))
    if a == random:
        print("Congratulations, You guess number after " + str(i) + " tries.")
        break
    elif a > random:
        print("Number is smaller")
    else:
        print("Number is bigger")

print("You had", i, "tries.")