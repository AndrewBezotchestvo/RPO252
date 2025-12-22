# localtime() — текущее локальное время как структура
import time

local = time.localtime()
print("Структура времени:")
print(f"  Год: {local.tm_year}")
print(f"  Месяц: {local.tm_mon}")
print(f"  День: {local.tm_mday}")
print(f"  Час: {local.tm_hour}")
print(f"  Минута: {local.tm_min}")
print(f"  Секунда: {local.tm_sec}")
print(f"  День недели: {local.tm_wday} (0=понедельник)")
print(f"  День года: {local.tm_yday}")
print(f"  Летнее время: {local.tm_isdst}")

# gmtime() — UTC время
utc_struct = time.gmtime()
print(f"\nUTC время: {time.strftime('%Y-%m-%d %H:%M:%S', utc_struct)}")