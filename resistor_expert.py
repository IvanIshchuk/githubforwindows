colors = ["green", "brown", "orange", "grey"]
color_dict = {'black': '0', 'brown': '1', 'red': '2', 'orange': '3', 'yellow': '4', 'green': '5', 'blue': '6', 'violet': '7', 'grey': '8', 'white': '9'}
color_tolerance = {'red': '2%', 'brown': '1%', 'green': '0.5%', 'blue': '0.25%', 'violet': '0.1%', 'grey': '0.05%', 'gold':  '5%', 'silver': '10%'}
name_kilo = ('ohms','kiloohms', 'megaohms', 'gigaohms')
numer = ""
amcol = len(colors)
count = 0
if amcol >= 3:
    for index in range(amcol - 2):
        numer = numer + color_dict[colors[index]]
    for _ in range(int(color_dict[colors[-2]])):
        numer = numer + '0'
    numer = float(numer)
    print(numer)
    while numer > 1000:
        number = numer % 1000
        numer /= 1000
        count += 1
    if number == 0:
        numer = int(numer)
    result = f"{numer} {name_kilo[count]} +-{color_tolerance[colors[-1]]}"
else:
    for index in range(amcol):
        numer = numer + color_dict[colors[index]]
    result = f"{int(numer)} {name_kilo[count]}"
        
    
#print(number)
print(result)