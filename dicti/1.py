# dict - словарь

user = {"name":"Тихон", "second name": "Шпехт", "age": 18}

#добавлять
user["password"] = "1234"
user.update({"login":"0000"})
user["age"] = 105

#удалять
user.pop("age")
del user["login"]

#выводить данные
print(user)
print(user["name"])  #обращение по ключу
print(user.items()) #выдать пары ключ значение
print(user.keys()) #выдать список ключей
print(user.values())  #выдать список значений