from datetime import datetime

now = datetime.now()

# Компоненты даты
print(f"Год: {now.year}")
print(f"Месяц: {now.month}")
print(f"День: {now.day}")
print(f"Час: {now.hour}")
print(f"Минута: {now.minute}")
print(f"Секунда: {now.second}")
print(f"День недели: {now.weekday()}")  # 0=понедельник
print(f"День года: {now.timetuple().tm_yday}")

# Замена компонентов
new_date = now.replace(year=2024, month=12)
print(f"Изменили год и месяц: {new_date}")