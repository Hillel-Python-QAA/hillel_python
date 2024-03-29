print('Hello, there')
# Введення
name = input('What is your name?: ')

# Конкатенація - поєднання рядка зі змінною
print('Nice to meet you ' + name)

age = input('How old are you?: ')

# format string
print('You are {} years old and your name is {}, that\'s nice'.format(age, name))
# escape symbols | Екранування
# **Екранування `\`:**
#
# - Використовується для екранування спеціальних символів в рядках, наприклад, `\'`, `\"`, `\\`.
#
# `рядок = 'Це символ екранування: \n Новий рядок.'`

# f-string
print(f'You are {age} years old and your name is {name}, that\'s nice')

age = int(age)
print('You are {:-9} years old and your name is {}, that\'s nice'.format(age, name))
print(f'You are {age:.3%} years old and your name is {name}, that\'s nice')
print('You have ' + str(age) + ' years')
print('You have ' + age.__str__() + ' years')

# PRINT
print('print function demo', age, name, sep=', ', end=' ')
print('end')
