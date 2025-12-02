#надите максимум в списке без функции max()

def find_max(list):
    max_number = list[0]

    for number in list:
        if number > max_number:
            max_number = number

    return max_number