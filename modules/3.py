from datetime import datetime

now = datetime.now()

formats = {
    "%d.%m.%Y": "Российский формат",
    "%Y-%m-%d": "Международный формат",
    "%A, %d %B %Y": "Полное название",
    "%H:%M:%S %d.%m.%Y": "Дата и время",
    "%c": "Локальное представление",
}

for fmt, desc in formats.items():
    print(f"{desc}: {now.strftime(fmt)}")

# Пример: создание имени файла с датой
filename = f"отчёт_{now.strftime('%Y-%m-%d_%H-%M')}.pdf"
print(f"Имя файла: {filename}")