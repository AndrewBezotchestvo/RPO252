# 6. Словарь заклинаний
#    Создайте словарь, где ключ — название заклинания,
# а значение — урон
# (Dictionary<string, int>). По имени заклинания
# выводите его силу

spells = {"Экспилиармус": 500, "Редукто": 100, "Круцио": 1500}

while True:
    spell = input("Введите название заклинания: ")

    is_spell = False

    for spell_name, power in spells.items():
        if spell.lower().strip() == spell_name.lower():
            print(f"преминено заклинание {spell_name}, с силой {power}")
            is_spell = True
            break

    if not is_spell:
        print("Заклинание не найдено")
