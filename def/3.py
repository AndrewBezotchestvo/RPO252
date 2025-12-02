#функция которая удаляет заданый элемент во всем списке
#функция в качетве параметра принимает список и заданый элемент
#и возвращает измененный список

def delete_element(list, element):
    new_list = []
    for item in list:
        if item != element:
            new_list.append(item)
    return new_list

new_list = delete_element([1, 2, 2, 2, 4, 3, 4, 5], 2)
print(new_list)

