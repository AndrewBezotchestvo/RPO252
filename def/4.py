#напишите функцию которая принимает 2 списка и
#возвращает новый список
#с общими элементами 2-х списков, без функции set

def union(list1, list2):
    union_numbers = []
    for item in list1:
        if item in list2 and item not in union_numbers:
            union_numbers.append(item)
    return union_numbers

list1 = [1, 2, 2, 2, 4, 3, 4, 5]
list2 = [1, 2, 4, 3, 4, 5, 6, 7, 8]
print(union(list1, list2))