# Из строки по формату
from datetime import datetime

date_str = "15.03.2024 14:30"
parsed_date = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
print(f"Распарсено: {parsed_date}")

print(f"дата: {parsed_date.date()}")
print(f"день: {parsed_date.day}")
print(f"час: {parsed_date.hour}")
print(f"минута: {parsed_date.minute}")
print(f"секунда: {parsed_date.second}")
print(f"секунда: {parsed_date.month}")
print(f"секунда: {parsed_date.isoweekday()}")

# Автоматический парсинг (ISO 8601)
iso_date = datetime.fromisoformat("2024-03-15")
print(f"ISO: {iso_date}")

# Из timestamp
timestamp = 100
dt_from_ts = datetime.fromtimestamp(timestamp)
print(f"Из timestamp: {dt_from_ts}")