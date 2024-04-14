color_dict = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
colors = ("red", "black", "red")
name_kilo = ('ohms','kiloohms', 'megaohms', 'gigaohms')
color_list =[]
num = ""
numer = ""
for item in colors:
    num = num + color_dict[item]
for key in color_dict:
    color_list.append(key)

if int(color_dict[colors[2]]) >= 2:
    count_zero = int(color_dict[colors[2]])
    if colors[1] == 'black':
        count_zero += 1
        count_killo = int(count_zero / 3)
        numer = color_dict[colors[0]]
        
        for index in range(count_zero % 3):
            numer = numer + '0'
        result = f"{int(numer)} {name_kilo[count_killo]}"
    else:
        count_killo = int(count_zero / 3)
        numer = color_dict[colors[0]] + color_dict[colors[1]]
        for index in range(count_zero % 3):
            numer = numer + '0'
        result = f"{int(numer)} {name_kilo[count_killo]}"
else:
    if colors[2] == 'black':
        numer = color_dict[colors[0]] + color_dict[colors[1]]
        result = f"{int(numer)} {name_kilo[0]}"
    else:
        numer = color_dict[colors[0]] + color_dict[colors[1]] + '0'
        result = f"{int(numer)} {name_kilo[0]}"
    
print(num)
print(result)