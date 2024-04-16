# Рахування унікальних символів в строці

my_string = str(input("Please, enter string: "))
unique_symbols = ""

for symbol in my_string:
    if symbol not in unique_symbols:
        unique_symbols += symbol
print("Unique symbols count: ", len(unique_symbols))


# Цикл “Дочекайся літери”

word = str(input("Please enter a word that contains \"h\" letter: "))

while word.lower().find("h") == -1:
    word = str(input("Please enter word that contains \"h\" letter: "))


# Забери зі списку що потрібно

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst_str = []
lst_int = []
lst_bool = []
for value in lst1:
    if type(value) is str:
        lst_str.append(value)
    elif type(value) is int:
        lst_int.append(value)
    elif type(value) is bool:
        lst_bool.append(value)
print(lst_str, lst_int, lst_bool)


# Сумуємо числа

my_list = list(range(1, 100, 3))
numbers_sum = 0
for number in my_list:
    if number % 2 == 0:
        numbers_sum += number
print(my_list)
print("The sum of all even numbers in the list is: ", numbers_sum)