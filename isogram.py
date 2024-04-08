string = 'six-yearx-old'
for index in range(len(string)):
    new_string = string[:index] + string[index + 1:]
    if string[index] in new_string and string[index].isalpha():
        print(string, 'is not')
        raise SystemExit
print('yes')