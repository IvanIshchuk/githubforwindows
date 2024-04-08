from cs50 import get_string
from sys import argv

while True:
    if len(argv) == 2 and argv[1].isalpha():
        break
    else:
        print("Usage: python vigener.py k")
        exit(1)

plaintext = get_string("plaintext: ")
print("ciphertext: ", end="")

key = argv[1]
k = 0

for a in plaintext:
    if a.isalpha():
        regalphakey = 65 if key[k].isupper() else 97
        numalphakey = ord(key[k]) - regalphakey
        regalpha = 65 if a.isupper() else 97
        numalpha = ord(a) - regalpha
        c = ((numalpha + numalphakey) % 26) + regalpha
        print(chr(c), end="")
        k += 1
        if k == len(key):
            k = 0
    else:
        print(a, end="")
print()
