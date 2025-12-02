# Проверка ввода: Создайте пустой
# список. В бесконечном цикле запрашивайте
# у пользователя ввод чисел. Если пользователь
# вводит не число, выводите сообщение об ошибке
# и запрашивайте ввод заново. Если пользователь
# ввел "exit", завершите программу.
# В конце выведите все введенные числа.
list1 = []
while True:
 try:
    x = input("введите число: ")
    if x == "exit":
         raise SystemExit
    list1.append(int(x))
 except ValueError:
     print("error, incorrect value")
 except SystemExit:
     print(f"{list1}")
     break



