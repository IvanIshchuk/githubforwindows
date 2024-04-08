isbn = '3-598-P1581-X'
new_isbn =""
sum = 0
isbn = isbn.replace("-", "")
if len(isbn) == 10:
    for symbol in isbn:
        if symbol.isnumeric():
            new_isbn = new_isbn + symbol
    if isbn[-1] == 'X':
        new_isbn = new_isbn + isbn[-1]
    print(new_isbn)
    if len(new_isbn) == 10:
        print(new_isbn)
        count = 10
        if new_isbn[-1] == 'X':
            for num in range(9):
                sum = sum + int(new_isbn[num]) * (count)
                count -= 1
            sum = (sum + 10) % 11
        else:
            for num in new_isbn:
                sum = sum + int(num) * (count)
                count -= 1
            print(sum)
            sum = sum % 11
            print(sum)
        if sum == 0:
            print('+')
            raise SystemExit
print('1-')