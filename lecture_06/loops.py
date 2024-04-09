x = 5;
y = 4
x, y = y, x

print('x=', x, ' y=', y)

# loop WHILE

count = 0
while count < 5:
    print(count)
    count += 1  # count += 1 == count = count + 1

word = 'Python'
index = 0
while index < len(word):
    print(word[index])
    index += 1

# FOR loop
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

message = 'Hello'
for char in message:
    print(char)

person = {"name": "John", "age": 30, "city": "New York"}
for key, value in person.items():
    print(key, ':', value)

for key in person.keys():
    # print(key)
    print(key, ':', person[key])

number_list = list(range(1, 40, 3))

print(number_list)
for i, value in enumerate(number_list):
    print('index: ', i, ' value: ', value)
    if value % 2 == 0:
        print('even number index: ', i)

for i in range(10):
    for j in range(i):
        print('*', end='')
    print('*')

# WHILE loop infinite
while True:
    age = input("How old are you?: ")
    if age in ['exit', 'quit']:
        break  # Зупиняє виконання циклу(петлі)
    if not age.isdigit():
        print(f'Given value: "{age}" is not an number, please correct it!')
        continue  # Продовжує цикл з нової ітерації
    age = int(age)
    if age < 18:
        print('Hello child')
    elif age < 40:
        print('Hello youth')
    else:
        print('Hello senior')


# BREAK AND CONTINUE

for i in range(10):
    if i % 2 == 0:
        continue
    print("Непарне число:", i)

for i in range(10):
    if i % 2 != 0:
        print("Непарне число:", i)
