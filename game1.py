# Задача 2: Создайте игру "Угадай слово".
# Программа случайным образом выбирает слово из списка.
# Пользователь пытается отгадать, вводя буквы.
# После каждой попытки выводится текущее состояние слова (например: п_т_н).
# Игра заканчивается, когда слово угадано или закончились попытки.
import random

words = ["Варвара", "Умар", "Артур", "Алексей"]

secret_word = random.choice(words)
user_word = len(secret_word) * "-"
print(user_word)
popitki = 5

print("добро пожаловать игру, угадайте все буквы и уйдите с призом или умрите! ")
while popitki > 0:
    letter = input("Введите букву: ")
    if len(letter) != 1:
        print("вы ввели более 1 символа")
        continue

    if letter not in secret_word:
        print("такой буквы нет")
        popitki -= 1
        print(f"осталось {popitki} попыток")
        continue

    user_list = list(user_word)
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            user_list[i] = letter

    user_word = "".join(user_list)
    print("Ваше слово:", user_word)


