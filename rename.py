import os

# Задайте шлях до папки з файлами
folder_path = r'C:\Users\31646\OneDrive\Home\Photo\2023\BD_2023'

# Отримайте список імен файлів у папці
files = os.listdir(folder_path)
counter = 1
# Пройдіться по кожному файлу у списку
for filename in files:
    # Розділіть ім'я файлу та його розширення
    name, extension = os.path.splitext(filename)
    # Складемо нове ім'я файлу з префіксом "new_" перед оригінальним ім'ям
    new_name = f'ДН_{counter:04d}_2023{extension}'
    # Складаємо старий та новий шлях до файлу
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path, new_name)
    # Перейменовуємо файл
    os.rename(old_path, new_path)
    counter += 1