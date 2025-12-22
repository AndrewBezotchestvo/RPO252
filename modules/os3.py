import os
import time

# with open('example.txt', 'w') as f:
#     f.write("Привет, мир!")

filename = 'example.txt'

# Проверки
print(f"Существует: {os.path.exists(filename)}")
print(f"Это файл: {os.path.isfile(filename)}")
print(f"Это папка: {os.path.isdir(filename)}")
print(f"Это ссылка: {os.path.islink(filename)}")

# Размер файла
if os.path.exists(filename):
    size = os.path.getsize(filename)
    print(f"Размер: {size} байт")

    # Человекочитаемый размер
    for unit in ['Б', 'КБ', 'МБ', 'ГБ']:
        if size < 1024:
            print(f"Размер: {size:.1f} {unit}")
            break
        size /= 1024

# Время модификации
mtime = os.path.getmtime(filename)  # Timestamp
print(f"Изменён: {time.ctime(mtime)}")