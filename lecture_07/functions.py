### Built-in functions in Python
# abs(x) - Повертає абсолютне значення (модуль) числа x

print('Модуль числа -10:', abs(-10))

# all() - Повертає True, якщо всі елементи в ітерабельному об'єкті істинні (або якщо об'єкт порожній).
print('all function with true outcome:', all([1, 2, 3]))  # True
print('all function with false outcome:', all([1, 2, 0]))  # False because of 0

# any() - Повертає True, якщо хоча б один елемент в ітерабельному об'єкті істинний.

# bin() - Повертає рядок, який представляє бінарне представлення цілого числа `x`.

# ascii() - Повертає читабельну версію об'єкта obj. Замінює символи, що не входять до ASCII, з їхніми escape-символами.
print(ascii('Україна'))  # "'\\u0423\\u043a\\u0440\\u0430\\u0457\\u043d\\u0430'"


# Створення функції

# def - ключове слово для визначення (створення) функції

# Function without arguments


def function_name():
    """Print 'Hello, World!'"""
    print('Hello, World!')


function_name()

# Function with arguments


def describe_pet(animal_type, pet_name):
    """
    Describe information about pet
    :param animal_type:
    :param pet_name:
    :return: f"My {animal_type}'s name is {pet_name.title()}"
    """
    return f"My {animal_type}'s name is {pet_name.title()}"


print(describe_pet('dog', 'oscar'))
print(describe_pet(pet_name='Akhil', animal_type='dog'))

# Function with default argument


def greet(name, greeting='Hi'):
    """
    Print greetings for given name
    :param name:
    :param greeting: Default value is 'Hi'
    :return: None
    """
    print(f"{greeting}, {name}")


greet('Yurii')
greet(name='Mr.Bond', greeting='Good afternoon')


# *args - list of arguments

def print_args(*args):
    print(args)
    for arg in args:
        print(arg)


print_args(1, 'Hello', 3.14, [1, 2, 3])
print_args(1)
# print(1_000_000.00)  1000000.0


# **kwargs

def print_kwargs(**my_kwa):
    print(my_kwa)
    for key, value in my_kwa.items():
        print(f"{key}: {value}")


print_kwargs(name='Yurii', age=35, city='Wroclaw')


# *args | **kwargs

def print_args_and_kwargs(*args, x,  a=10, **kwargs):
    print(args)
    for arg in args:
        print(arg)

    print(x)
    print(a)

    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_args_and_kwargs(1, 'Hello', 3.14, [1, 2, 3], x=1, a=3, name='Yurii', age=35, city='Wroclaw')

# Lambda function
# lambda arguments: expression

square = lambda x: x**2
print(square(5))  # 25

x_power_y = lambda x, y: x ** y
print(x_power_y(2, 3))  # 8


print(min(2, 3))
lambda_min = lambda x, y: x if x < y else y

print(lambda_min(2,3))


# map()

base_numbers = [2, 4, 6, 8, 10]
powers = [1, 2, 3, 4, 5]
numbers_powers = list(map(pow, base_numbers, powers))

print(numbers_powers)  # [2, 16, 216, 4096, 100000]

lambda_powers = list(map(lambda x: x ** x, base_numbers))

print(lambda_powers)


# zip()
list1 = (1, 2, 3)
list2 = ('a', 'b', 'c', 'd')
list3 = (4, 5, 6, 6)

zipped = zip(list2, list1, list3)
print(zipped)
print(tuple(zipped))

# enumerate

list4 = [1, 2, 3, 4, 5, 6, 7, 8]

for i, value in enumerate(list4):
    print(f"value: {value} at index: {i}")

list5 = ['banana', 'apple', 'plum']
print(dict(enumerate(list5)))

# eval(expression, globals=None, locals=None)

exp_one = '3 + 5 * 2'
print(eval(exp_one))  # 13

x = 10
y = 20
print(eval('x + y'))  # 30


# exec(object[, globals[, locals]])

code_block = """
result = x + y
print(f"Result: {result}")
"""

exec(code_block)


# compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

code = """
def greetings(name):
    print(f"Hello, {name}")
    
greetings('Yurii')
"""

compiled_code = compile(code, '<string>', 'exec')
# print(compiled_code)

exec(compiled_code)

compiled_exp = compile(exp_one, '<string>', 'eval')

result = eval(compiled_exp)
print(result)  # 13
