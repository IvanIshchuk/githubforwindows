question = 'What is 3 plus 2 multiplied by 3?'
if question[-1] != '?':
    raise ValueError("syntax error")
question = question[:-1]
words = question.split()
print(question)