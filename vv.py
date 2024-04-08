number = 1
#def steps(number):
if number <= 0:
        raise ValueError("Only positive integers are allowed")
count = 1
while number != 1:
    count += 1
    if number % 2 == 0:
        number /= 2
        #count += 1
        continue
    else:
        number = number * 3 + 1
        #count +=1
print(count)
