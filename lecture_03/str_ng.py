_string = "Hello, world!"

print(_string)

# Indexes
print(_string[0]) # H
print(_string[1]) # e
print(_string[2]) # l

print(_string[-1]) # !
print(_string[-2]) # d
print(_string[-3]) # l

# length
print(len(_string))
print(_string.__len__())

# Slices
# iterable[start:stop:step]
# - `start`: Початковий індекс (не включаючи).
# - `stop`: Кінцевий індекс (включно).
# - `step`: Крок, з яким вибираються елементи (за замовчуванням 1).

# slice from first element
print(_string[0:])

# slice from n-th element

print(_string[3:])

# slice from the last element
print(_string[:-1])

# slice for reverse string
print(_string[::-1])

# slice start + end
print(_string[:6])

# Ітерації
for char in _string:
    print(char)

# SPLIT
shopping_list = 'apple, banana, pineapple, eggs, milk'
print(shopping_list)
items = shopping_list.split(', ')
print(items)
new_items = ' and '.join(items)
print(new_items)
print(new_items.split(' and '))

# startswith
if _string.startswith('Hello'):
    print('Greetings!')
else:
    print('No greetings!')

# endswith

if _string.endswith('world!'):
    print('world!')
else:
    print('etc!')

# перевірка на регістр
print(_string.islower())
print(_string.isupper())
print(_string.istitle())

print(_string)
print(_string.upper())
print(_string.lower())
print(_string.title())
print(_string.swapcase())

# find
_string = "Це приклад для пошуку у рядку."
index = _string.find('пошук')
print(index)

# replace
_string = "Це приклад для заміни у рядку."
print(_string)
new_string = _string.replace('заміни', 'підміни')
print(new_string)
_string = "Це приклад для заміни у рядку, заміни лише перше входження."
print(_string)
new_string = _string.replace('заміни', 'підміни', 1)
print(new_string)


# strip | lstrip | rstrip

_string = "    Привіт, світ!    "
print(_string)
new_string = _string.strip()
print(new_string)

print(_string.lstrip())
print(_string.rstrip())

#
_string = "1,2,3,4,5"
new_string = _string.replace(',', ':')
print(new_string)
_list = [int(item) for item in _string.split(',')]
print(_list)
print(_list[::-1])
print(_string[::-1])


