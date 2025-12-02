# Описание задачи: Напишите программу
# add_elements, которая принимает два списка
# одинаковой длины и выводит новый список, в котором
# каждый элемент является суммой элементов из двух списков
# на той же позиции. Если списки имеют разную длину,
# выбросите исключение IndexError с сообщением ("Списки "
#                                               "должны быть "
#                                               "одинаковой длины").
# Если любой элемент в списке не является числом, выбросите исключение
# ValueError с
# сообщением "Списки должны содержать только числа".

def add_ellements(list1, list2):
    global list3
    try:
        list3 = []
        for i in range(len(list1)):
            num1 = int(list1[i])
            num2 = int(list2[i])
            list3.append(num1 + num2)
        if len(list1) != len(list2):
            raise IndexError
        return list3
    except IndexError:
        print("списки не одинаковой длины")
        return list3
    except ValueError:
        print("возникла ошибка преобразования")
        return list3

list1 = [1, 2, 32, "5f", 0]
list2 = [6, 7, 8, 9, 6, 8]
print(add_ellements(list1, list2))

