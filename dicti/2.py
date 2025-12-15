# Словарь `Dictionary<string, string>` хранит
# описание локаций. Игрок вводит название локации и
# получает её описание.
# Также добавьте возможность добавлять локацию и удалять
# локацию
import json

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4 ,ensure_ascii=False)

def show_all_locations(locations: dict):
    if locations:
        for location, discription in locations.items():
            print(f"Название локации: {location} \nОписание локации: {discription} \n\n")
    else:
        print("нет локаций")


def add_location(locations: dict):
    name = input("Напишите название локации: ")
    disription = input("Напишите описание локации: ")

    if name and disription:
        locations[name] = disription
        print(f"Добавлена локация: {name} \nОписание локации: {disription} \n")
    else:
        print("не все данные введены")

    return locations


def delete_location(locations: dict):
    name = input("Напишите название локации: ")
    if name in locations.keys():
        locations.pop(name)
        print(f"Локация {name} удалена")
    else:
        print("Такой локации не существует")

    return locations


def show_disriptions(locations: dict):
    name = input("Напишите название локации: ")
    if name in locations.keys():
        print(f"описание локации {name} - {locations[name]}")
    else:
        print("Данной локации не существует")

locations = load_json("locations.json")

while True:
    print("\n1. Отобразить все локации",
          "2. Добавить локацию",
          "3. Удалить локацию",
          "4. Найти описание локации", sep="\n")
    action = input("Введите команду:")

    match action.strip():
        case "1":
            show_all_locations(locations)
        case "2":
            locations = add_location(locations)
        case "3":
            locations = delete_location(locations)
        case "4":
            show_disriptions(locations)
        case _:
            print("неверная команда")

    save_json("locations.json", locations)