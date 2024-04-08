from cs50 import get_string
from sys import argv


message = get_string("What message would you like to censore?\n")
for a in message[3]:
    print(a," ", end="")
print()
