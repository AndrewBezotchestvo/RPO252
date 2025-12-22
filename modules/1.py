import datetime
#from datetime import datetime, date, time, timedelta, timezone
# Текущая дата и время
now = datetime.datetime.now()
print(f"Сейчас: {now}")

# Конкретная дата
birthday = datetime.datetime(1995, 8, 15, 14, 30)  # год, месяц, день, час, минута
print(f"День рождения: {birthday}")

# Только дата
today = datetime.date.today()
print(f"Сегодня: {today}")

# Только время
meeting_time = datetime.time(9, 30, 0)  # 09:30:00
print(f"Время встречи: {meeting_time}")

