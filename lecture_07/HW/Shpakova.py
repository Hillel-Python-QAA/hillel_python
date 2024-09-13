# task 1
"""Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""


def multiplication_table(number):
    """
    :param number:number for multiplication
    :return: multiplication until product is more than 25
    """
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while number * multiplier <= 25:
        result = number * multiplier
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        # Increment the appropriate variable
        multiplier += 1


multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""


def two_numbers_sum(number_1, number_2):
    """

    :param number_1:
    :param number_2:
    :return: sum of two numbers
    """
    return number_1 + number_2


print(two_numbers_sum(2, 4))

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""


def avg_number(numbers_list):
    """

    :param numbers_list: list of numbers
    :return: average for numbers in list
    """
    return sum(numbers_list) / len(numbers_list)


my_list = [2, 2, 5]

print(avg_number(my_list))


# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""


def reversed_line(line: str):
    """

    :param line: some string
    :return: reversed string
    """
    reversed_list_from_line = list(line)[::-1]
    new_line = "".join(reversed_list_from_line)
    return new_line


print(reversed_line("ab cd"))

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""


def longest_word_search(words_list):
    """

    :param words_list:
    :return: longest word in the list
    """
    longest_word = ""
    for word in words_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""


def find_substring(str1, str2):
    """

    :param str1:
    :param str2:
    :return: if str1 contains str2, returns index of str2 in str1; if not, returns -1
    """
    return str1.find(str2)


str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2))  # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2))  # поверне -1

# task 7
# Рахування унікальних символів в строці


def unique_symbols_count(string):
    """
    :param string:
    :return: count of unique symbols in string
    """
    unique_symbols = ""
    for symbol in string:
        if symbol not in unique_symbols:
            unique_symbols += symbol
    return len(unique_symbols)


print(unique_symbols_count("tkjjfkgkfj"))


# task 8
def filter_list_by_value(list1, value):
    """
    :param list1: list with items of any type
    :param value: str, int or bool
    :return: filtered list
    """
    new_list = []
    for item in list1:
        if type(item) is value:
            new_list.append(item)
    return new_list


my_list = [6, 8, "jjh", True, True, False, "hj"]
print(filter_list_by_value(my_list, bool))

# task 9
cars_list = {
    "Mercedes": ("silver", 2019, 1.8, "sedan", 50000),
    "Audi": ("black", 2020, 2.0, "sedan", 55000),
    "BMW": ("white", 2018, 3.0, "suv", 70000),
    "Lexus": ("gray", 2016, 2.5, "coupe", 45000),
    "Toyota": ("blue", 2021, 1.6, "hatchback", 25000),
    "Honda": ("red", 2017, 1.5, "sedan", 30000),
    "Ford": ("green", 2019, 2.3, "suv", 40000),
    "Chevrolet": ("purple", 2020, 1.4, "hatchback", 22000),
    "Nissan": ("pink", 2018, 1.8, "sedan", 35000),
    "Volkswagen": ("brown", 2021, 1.4, "hatchback", 28000),
    "Hyundai": ("gray", 2019, 1.6, "suv", 32000),
    "Kia": ("white", 2020, 2.0, "sedan", 28000),
    "Volvo": ("silver", 2017, 1.8, "suv", 45000),
    "Subaru": ("blue", 2018, 2.5, "wagon", 35000),
    "Mazda": ("red", 2019, 2.5, "sedan", 32000),
    "Porsche": ("black", 2017, 3.0, "coupe", 80000),
    "Jeep": ("green", 2021, 3.0, "suv", 50000),
    "Chrysler": ("gray", 2016, 2.4, "sedan", 22000),
    "Dodge": ("yellow", 2020, 3.6, "suv", 40000),
    "Ferrari": ("red", 2019, 4.0, "coupe", 500000),
    "Lamborghini": ("orange", 2021, 5.0, "coupe", 800000),
    "Maserati": ("blue", 2018, 4.7, "coupe", 100000),
    "Bugatti": ("black", 2020, 8.0, "coupe", 2000000),
    "McLaren": ("yellow", 2017, 4.0, "coupe", 700000),
    "Rolls-Royce": ("white", 2019, 6.8, "sedan", 500000),
    "Bentley": ("gray", 2020, 4.0, "coupe", 300000),
    "Jaguar": ("red", 2016, 2.0, "suv", 40000),
    "Land Rover": ("green", 2018, 3.0, "suv", 60000),
    "Tesla": ("silver", 2020, 0.0, "sedan", 60000),
    "Acura": ("white", 2017, 2.4, "suv", 40000),
    "Cadillac": ("black", 2019, 3.6, "suv", 55000),
    "Infiniti": ("gray", 2018, 2.0, "sedan", 35000),
    "Lincoln": ("white", 2021, 2.0, "suv", 50000),
    "GMC": ("blue", 2016, 1.5, "pickup", 30000),
    "Ram": ("black", 2019, 5.7, "pickup", 40000),
    "Chevy": ("red", 2017, 2.4, "pickup", 35000),
    "Dodge Ram": ("white", 2020, 3.6, "pickup", 45000),
    "Ford F-Series": ("gray", 2021, 3.5, "pickup", 50000),
    "Nissan Titan": ("silver", 2018, 5.6, "pickup", 35000),
}


def car_searcher(cars_list, year, engine, price):
    """

    :param cars_list:
    :param year:
    :param engine:
    :param price:
    :return: list of sorted cars thar match criteria
    """
    matched_cars = dict()

    for car in cars_list:
        if (
            cars_list[car][1] >= year
            and cars_list[car][2] >= engine
            and cars_list[car][4] <= price
        ):
            matched_cars[car] = cars_list[car]
    sorted_matched_cars = dict(sorted(matched_cars.items(), key=lambda v: v[1][4]))
    return sorted_matched_cars


print(car_searcher(cars_list, 2017, 1.6, 36000))


# task 10
def items_swapper(list1, index1: int, index2: int):
    """
    :param list1:
    :param index1:
    :param index2:
    :return: list with swapped items
    """
    list1[index1], list1[index2] = list1[index2], list1[index1]
    return list1


my_list = ["One", "Two", "Three", "Four", "Five", "Six"]
print(items_swapper(my_list, 2, 4))

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# Додаткові завдання

# Рядок відформатованої дати:


def date_in_string(day: int, month: int, year: int, sep="."):
    """

    :param day:
    :param month:
    :param year:
    :param sep:
    :return: date in string format divided by separator
    """
    date_list = [str(day), str(month), str(year)]
    return sep.join(date_list)


print(date_in_string(3, 2, 4, "/"))


# Порівняння словників
def compare_grades(grades1, grades2):
    compared_grades = {}
    for key in grades1:
        if key in grades1 and key in grades2:
            compared_grades[key] = grades1[key] - grades2[key]
        elif key not in grades2:
            compared_grades[key] = grades1[key]
    for key in grades2:
        if key not in grades1:
            compared_grades[key] = grades2[key]

    return compared_grades


# Приклад використання функції:
grades_1 = {
    "Анна Коваленко": 90,
    "Олег Петров": 85,
    "Ірина Сидорова": 78,
    "Khhj IJj": 89,
}
grades_2 = {
    "Анна Коваленко": 92,
    "Олег Петров": 87,
    "Ірина Сидорова": 80,
    "iuiui IJj": 89,
}

result = compare_grades(grades_1, grades_2)
print(result)
