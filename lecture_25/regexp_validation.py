import re

email = "user@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Email введено правильно.")
else:
    print("Некоректний формат email.")