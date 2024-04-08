from cs50 import get_string
from sys import argv

while True:
    if len(argv) == 2:
        break
    else:
        print("Use python caesar.py k")
        exit(1)

keynum = int(argv[1])
plaintext = get_string("plaintext: ")
print("ciphertext: ", end="")
k = int(argv[1])
for a in plaintext:
    if a.isalpha():
        regalpha = 65 if a.isupper() else 97
        numalpha = ord(a) - regalpha
        c = ((numalpha + k) % 26) + regalpha
        print(chr(c), end="")
    else:
        print(a, end="")
print()
