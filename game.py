# Задача 1: Реализуйте текстовый квест:
# Игрок начинает с 100 здоровья.
# Каждое действие (например, войти в пещеру, убежать от монстра) случайно влияет на здоровье.
# Игра заканчивается, когда здоровье <= 0 или игрок достигает цели (например, найти сокровище).


quest_actions = {
    "start":{"description":"вы оказались в пещере", "choices":["найти выход", "пойти в пещеру"], "hp": [0, 10], "next_action":["выход", "пещера"]},
    "пещера":{"description":"Вы ушли глубще в пещеру и увидели кости", "choices":["пойти дальше", "выйти из пещеры"], "hp": [20, 10], "next_action":["глубже", "выход"]},
    "выход":{"description":"вы вышли из пещеры и увидели лес", "choices":["пойти в лес", "вернуться в пещеру"], "hp": [0, 10], "next_action":["лес", "start"]}
}

player_hp = 100
key = "start"

while player_hp > 0:
    print(quest_actions[key]["description"])
    print("сделайте выбор: ", " / ".join(quest_actions[key]["choices"]))
    next_action = input("введите текстом следующее действие: ")
    if next_action in quest_actions[key]["choices"]:
        player_hp -= quest_actions[key]["hp"][quest_actions[key]["choices"].index(next_action)]
        print("остаток hp", player_hp)
        key = quest_actions[key]["next_action"][quest_actions[key]["choices"].index(next_action)]
    else:
        print("такого действия нету")