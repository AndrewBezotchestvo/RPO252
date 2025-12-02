# Удаление дубликатов: Создайте
# список для хранения вводимых чисел.
# При вводе нового числа проверяйте,
# есть ли оно уже в списке. Если есть,
# игнорируйте его и выведите сообщение.
# Если пользователь введет "exit",
# выведите список уникальных чисел.

uniq_list = []
while True:
    try:
        number = input("введите число: ")
        if number == "exit":
            raise SystemExit
        if number in uniq_list:
            raise IndexError
        uniq_list.append(int(number))
    except IndexError:
        print("такой элемент уже есть")
    except ValueError:
        print("не верный тип данных")
    except SystemExit:
        print(uniq_list)
        raise SystemExit
