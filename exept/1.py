
list_numbers = []

#try: - попробовать, внутри пишем саму программу
#except тип ошибки: - исключение, код который
# выполниться при возникновении ошибки
#else - иначе, код который выполниться, если не вызвалась
# ни одна из ошибок
#raise - вызвать определенную ошибку
while True:
    try:
        number = int(input("введите число: "))
        list_numbers.append(number)
        if number < 0:
            raise TypeError
    except ValueError:
        print("элемент не добавлен, вы ввели не корректное значение")
    except TypeError:
        print("цикл остановился")
        break
    else:
        print("элемент добавлен")
    finally:
        print(f"в списке {len(list_numbers)}")
