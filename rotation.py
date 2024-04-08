key = 13
text = "abcdefghijklmnopqrstuvwxyz"
new_text = ""
if key < 0:
        raise ValueError("Only positive integers")
for letter in text:
    if letter.isalpha():
        if letter.isupper():
            new_letter = chr((ord(letter) - 65 + key) % 26 + 65)
            new_text = new_text + new_letter
        else:
            new_letter = chr((ord(letter) - 97 + key) % 26 + 97)
            new_text = new_text + new_letter
    else:
        new_text = new_text + letter
print(new_text)
