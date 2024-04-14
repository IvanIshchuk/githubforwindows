import re
question = 'What is 3 plus 2 multiplied by 3?'
if question[-1] != '?' and question[0] != 'What' and question[1] != 'is':
    raise ValueError("syntax error")
question = question[:-1]
question = re.sub(r'\bwhat is\b', '', question, flags=re.IGNORECASE)
question = re.sub(r'\bplus\b', '+', question, flags=re.IGNORECASE)
question = re.sub(r'\bmultipli(?:ed by)?\b', '*', question, flags=re.IGNORECASE)
    
    # Знаходимо числові значення
numbers = re.findall(r'\d+', question)
    
    # Повертаємо математичний вираз
#return sentence.format(*numbers)
#question = question.split()
#question = question[1:]

#words = question.split()
print(question)