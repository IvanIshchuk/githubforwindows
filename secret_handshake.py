binary_str = "10011"
actions = ('jump', 'close your eyes', 'double blink', 'wink')
secret_actions = []
for digit in range(-1, -5, -1):
    if binary_str[digit] == '1':
        secret_actions.append(actions[digit])
if binary_str[0] == '1':
    secret_actions.reverse()
    
        
print(secret_actions)
#print(binary_str[0])