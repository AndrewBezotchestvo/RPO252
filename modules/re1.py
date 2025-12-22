import re

# Поиск паттернов
text = "Мои номера: +7-999-123-45-67, +1-234-567-8900"
phone_pattern = r'\+\d{1,3}-\d{3}-\d{3}-\d{2,4}'
phones = re.findall(phone_pattern, text)
print(f"Найдены номера: {phones}")

# Валидация email
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(validate_email("student@university.ru"))  # True
print(validate_email("invalid@email"))          # False

# Замена текста
text = "Цена: 100$, Цена: 200$"
new_text = re.sub(r'\d+\$', 'XXX', text)
print(new_text)  # "Цена: XXX, Цена: XXX"