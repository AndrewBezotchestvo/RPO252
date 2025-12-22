# Текущее время в секундах с 1970
import time

timestamp = time.time()
print(f"Unix timestamp: {timestamp}")
print(f"Человекочитаемо: {time.ctime(timestamp)}")

# Пауза в выполнении
print("Начало работы...")
for i in range(3, 0, -1):
    print(f"Осталось {i}...")
    time.sleep(1)  # Пауза 1 секунда
print("Поехали!")
