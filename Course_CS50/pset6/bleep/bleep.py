from cs50 import get_string
from sys import argv

words = set()

def main():
    while True:
        if len(argv) == 2:
            break
        else:
            print("Usage: python bleep.py dictionary")
            exit(1)

    wordsban = argv[1]
    load(wordsban)

    message = get_string("What message would you like to censore?\n")
    wordmess = message.split()
    for word in wordmess:
        s = check(word)
        if s:
            l = list(word)
            for a in l:
                print("*", end="")
            print(" ", end="")
        else:
            print(word, "", end="")
    print()

def load(wordsban):
    try:
        with open(wordsban, "r") as file:
            for line in file:
                words.add(line.rstrip("\n"))
    except:
        exit(1)

def check(word):
    return word.lower() in words


if __name__ == "__main__":
    main()
