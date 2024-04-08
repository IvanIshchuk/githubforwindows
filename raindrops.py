number = 12
numbers = (3, 5, 7)
words = ('Pling', 'Plang', 'Plong')
word = ""
for num in range(3):
    if number % numbers[num] == 0:
        word = word + words[num]
        print(word)
    print(number)