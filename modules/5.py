from datetime import timezone, timedelta, datetime

# UTC время
utc_now = datetime.now(timezone.utc)
print(f"UTC время: {utc_now}")

# Создание своего часового пояса
moscow_tz = timezone(timedelta(hours=3))  # UTC+3
moscow_time = datetime.now(moscow_tz)
print(f"Москва: {moscow_time}")

# Конвертация между поясами
ny_tz = timezone(timedelta(hours=-5))  # UTC-5
ny_time = moscow_time.astimezone(ny_tz)
print(f"Нью-Йорк: {ny_time}")