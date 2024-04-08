import string
sentence = '"Five quacking Zephyrs jolt my wax bed."'
alphabet = string.ascii_lowercase
num = 0
sentence = sentence.lower()
for alpha in alphabet:
    if alpha in sentence:
        num +=1
if num == 26:
    print('pangram')
else:
    print('not pangram')

    
        