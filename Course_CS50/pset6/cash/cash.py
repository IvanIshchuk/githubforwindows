from cs50 import get_float

while True:
    change = get_float("Change owed: ")
    if change >= 0:
        break

cash = round(change * 100)

m25 = cash // 25
cash = cash % 25
m10 = cash // 10
cash = cash % 10
m5 = cash // 5
cash = cash % 5

coins = cash + m25 + m10 +m5

print(coins)
