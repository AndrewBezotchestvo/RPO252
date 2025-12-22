# Создание папки
import os

os.mkdir('test_folder')  # Одна папка
os.makedirs('data/images/2024', exist_ok=True)  # Рекурсивно

# # Создание файлов
with open('test_folder/file1.txt', 'w') as f:
    f.write("Привет, мир!")

# # Копирование, перемещение, удаление
import shutil  # Часто используется с os
#
# # Копирование файла
shutil.copy('test_folder/file1.txt', 'test_folder/file2.txt')

# # Переименование/перемещение
os.rename('test_folder/file2.txt', 'test_folder/renamed.txt')

# Удаление
os.remove('test_folder/renamed.txt')  # Файл
os.rmdir('test_folder')  # Пустую папку
shutil.rmtree('test_folder')  # Папку с содержимым (осторожно!)