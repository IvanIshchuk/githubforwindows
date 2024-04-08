from cs50 import get_int

while True:
    h = get_int("Height: ")
    if h >= 1 and h <= 8:
        break

for x in range(h):
    a = x + 1
    c = h - a
    print(" " * c, "#" * a, sep="")
