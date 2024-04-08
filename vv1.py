
def main():
    passengers = ['Jerimiah', 'Eric', 'Bethany', 'Byte', 'SqueekyBoots', 'Bob']
    number = len(passengers)
    print(number)
    dict_passenger = {}
    num_seat = simple_generator(number)
    for name, seat in zip(passengers, num_seat):
        dict_passenger[name] = seat
    print(dict_passenger)
    
def simple_generator(number):
    rows = number // 4
    last_row = number % 4
    seats = ['A', 'B', 'C', 'D']
    for c in range(rows):
        for seat in seats:
            num = str(c + 1)
            yield (num + seat)
    for i in range(last_row):
        num_last_row = str(rows + 1)
        yield (num_last_row + seats[i])
        
      
if __name__ == "__main__":
    main()
     
        
# Використання генератора

#for value in gen:
 #   print(value)