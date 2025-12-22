# Объединение путей (кросс-платформенно)
import os

path = os.path.join('home', 'user', 'documents', 'report.pdf')
print(f"Путь: {path}")

# Разделение пути
dirname, filename = os.path.split(path)
print(f"Папка: {dirname}")
print(f"Файл: {filename}")

# Расширение файла
basename, extension = os.path.splitext(filename)
print(f"Имя: {basename}")
print(f"Расширение: {extension}")

# Абсолютный путь
abs_path = os.path.abspath('.')
print(f"Абсолютный путь: {abs_path}")

# Нормализация пути (убирает ../ и ./)
complex_path = 'folder/.././subfolder/file.txt'
normalized = os.path.normpath(complex_path)
print(f"Нормализовано: {normalized}")

# Путь относительно другой директории
rel_path = os.path.relpath('/usr/bin/python', '/usr')
print(f"Относительный путь: {rel_path}")  # bin/python