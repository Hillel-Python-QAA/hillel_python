# Списки ( List )
# Форма запису
empty_list = []
empty_list_2 = list()

print(empty_list)
print(empty_list_2)
print(type(empty_list))
print(type(empty_list_2))

# Операції зі списками

_list = ['MON', 'TUE', 'WED', 'THU', 'FRI']

print(_list[0])  # MON
print(_list[4])  # FRI
print(_list[-1])  # FRI
print(_list[-5])  # MON

# Slices - list[start:stop:step]
# start - included
# stop - not included

_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
sub_list = _list[::2]
print(_list[::-1])
print(_list)
print(_list.reverse())
print(_list)
print(list(reversed(_list)))
print(_list)
print(sub_list)

# append()

my_list = [1, 2, 3]
print(my_list)

my_list.append(4)
print(my_list)

# extend
list1 = [1, 2, 3]
list2 = [4, 5, 6]
tuple1 = (7, 8, 9)

list1.extend(list2)

print(list1)

list1.extend(tuple1)
print(list2)

print(list1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# insert()
list3 = [1, 2, 3]
list3.insert(1, 4)
print(list3)  # [1, 4, 2, 3]

# remove() - видаляє перший елемент зі списку із вказаним значенням
list4 = [1, 2, 3, 2]
print(list4.remove(2))
print(list4)  # [1, 3, 2]

# pop() - видаляє елемент за індексом, або  останній елемент за замовчуванням
list5 = [1, 2, 3, 4]
print(list5.pop())  # 4
print(list5)  # [1, 2, 3]
print(list5.pop(1))  # 2
print(list5)  # [1, 3]

# index() - same as tuple

# count() - same as tuple

# Розпакування
print('Розпакування')
numbers = [1, 2, 3, 4, 5]
first, *middle, last = numbers
# *middle - зірочка вказує на те що елементів має бути більш ніж один
print(first)  # 1
print(middle)  # [2, 3, 4]
print(last)  # 5

# Сортування
# sort i sorted
numbers = [5, 2, 8, 1, 3]
sorted_numbers = sorted(numbers)
print(sorted_numbers)
sorted_numbers_reverse = sorted(numbers, reverse=True)
print(sorted_numbers_reverse)

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)


# Формування списків з інших типів даних
# list from string

my_string = "Hello, world!"
list_from_str = list(my_string)
print(list_from_str)

# list from range
my_range = range(1, 6)
list_from_range = list(my_range)
print(list_from_range)

# list from tuple
my_tuple = (1, 2, 3, 4, 5)
list_from_tuple = list(my_tuple)
print(list_from_tuple)

# list comprehension
squares = [x ** 2 for x in range(10)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

words = ["яблуко", "груша", "апельсин"]
words_lengths = [len(word) for word in words]
print(words_lengths)