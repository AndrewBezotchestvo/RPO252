from datetime import datetime, timedelta

now = datetime.now()

# Добавление интервалов
tomorrow = now + timedelta(days=1)
in_3_hours = now + timedelta(hours=3)
next_week = now + timedelta(weeks=1)

print(f"Завтра: {tomorrow}")
print(f"Через 3 часа: {in_3_hours}")

# Разница между датами
new_year = datetime(2026, 1, 1)
time_left = new_year - now
print(f"До нового года: {time_left.days} дней")
print(f"Часов: {time_left.total_seconds() / 3600:.1f}")

# Сравнение дат
date1 = datetime(2024, 3, 15)
date2 = datetime(2024, 3, 20)
print(f"date1 < date2: {date1 < date2}")
print(f"date1 == date2: {date1 == date2}")