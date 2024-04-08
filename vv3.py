class SimpleIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value

# Створюємо ітератор
my_iterator = SimpleIterator([1, 2, 3, 4, 5])

# Використовуємо ітератор
print(next(my_iterator))  # Виводить 1
print(next(my_iterator))  # Виводить 2
print(next(my_iterator))  # Виводить 3
print(next(my_iterator))  # Виводить 3
print(next(my_iterator))  # Виводить 3
print(next(my_iterator))  # Виводить 3