question = 'What is 1 2 plus?'
question = question.replace('plus', '+').replace('multiplied by', '*').replace('minus', '-').replace('divided by', '/').replace('?', '').replace('What', '').replace('is', '').strip()
#expression = question.split()
print(question)