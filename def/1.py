#написать функцию которая создает список по заданным параметрам (количество элементов,
# диапазон значений) и возвращает его в значение функции
import random

def generate(n, min, max):
    numbers = []
    for i in range(n):
        numbers.append(random.randint(min, max))

    return numbers

print(generate(5, 4, 4))
