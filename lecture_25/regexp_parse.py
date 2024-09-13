import re

# Текст для пошуку
text = "Телефонний номер: 123-456-7890"

# Регулярний вираз для пошуку телефонних номерів
pattern = r"\d{3}-\d{3}-\d{4}"

# Пошук телефонного номера у тексті
phone_number = re.search(pattern, text)

if phone_number:
    print("Знайдено телефонний номер:", phone_number.group())
else:
    print("Телефонний номер не знайдено")
