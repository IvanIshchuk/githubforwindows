from cs50 import get_string
from sys import argv


message = get_string("What message would you like to censore?\n")
b = message.split()
for a in message:
    print(a," ", end="")
    #l = list(a)
    for c in a:
        print("*", end="")
    print(" ", end="")
print()
