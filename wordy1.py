question = 'What is 1 2 plus?'
question = question.replace('plus', '+').replace('multiplied by', '*').replace('minus', '-').replace('divided by', '/').replace('?', '').replace('What', '').replace('is', '').strip()
expression = question.split()
print(expression)
for symbol in expression:
    try:
        int(symbol)   
    except:
        if not symbol in ['+', '-', '*', '/']:
            raise ValueError("unknown operation")
           
try:
    result = int(expression[0])
    for index in range(1, len(expression), 2):
        if expression[index] == '+':
            result += int(expression[index + 1])
        elif expression[index] == '-':
            result -= int(expression[index + 1])
        elif expression[index] == '*':
            result *= int(expression[index + 1])
        elif expression[index] == '/':
            result /= int(expression[index + 1])
        else:
            raise ValueError("syntax error")
except:
    raise ValueError("syntax error")
print('end', result)

    
    