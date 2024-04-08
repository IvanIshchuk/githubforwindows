# American Express: lnumcard = 15, firstdigits = 34 or 37
# MasterCard: lnumcard = 16, firstdigits = 51, 52, 53, 54 or 55
# Visa: lnumcard = 13 or 16, firstdigits = 4

while True:
    numcard = input("Number: ")
    if numcard.isdigit():
       break

lnumcard = len(numcard)

sumfirstdigit = 0
sumseconddigit = 0
if lnumcard == 13 or lnumcard == 15 or lnumcard == 16:
    y = -1
    n = 1
    for x in numcard:
        if n % 2 != 0:
            sumfirstdigit = int(numcard[y]) + sumfirstdigit
        else:
            sum1 = int(numcard[y]) * 2
            sumseconddigit += (sum1 // 10) + (sum1 % 10)
        y -= 1
        n += 1
        sumalldigits = sumfirstdigit + sumseconddigit
        firstdigits = int(numcard[0] + numcard[1])

    if sumalldigits % 10 == 0 and lnumcard == 15 and (firstdigits == 34 or firstdigits == 37):
        print("AMEX")
    elif  sumalldigits % 10 == 0 and lnumcard == 16 and firstdigits >=51 and firstdigits <=55:
        print("MASTERCARD")
    elif sumalldigits % 10 == 0 and (lnumcard == 13 or lnumcard == 16) and firstdigits // 10 == 4:
        print("VISA")
else:
    print("INVALID")
