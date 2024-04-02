# Tuple ( Кортеж )
# Форма запису

empty_tuple = ()
empty_tuple_2 = tuple()
print(empty_tuple)
print(empty_tuple_2)
print(type(empty_tuple))
print(type(empty_tuple_2))

single_el_tuple = (42,)
print(single_el_tuple)
print(type(single_el_tuple))

mixed_tuple = (1, 'hello', 3.14, True)
print(mixed_tuple)
print(type(mixed_tuple))

rare_form_tuple = 1, 'hello', 3.14, True
print(rare_form_tuple)
print(type(rare_form_tuple))

# Доступ до елементів
my_tuple = (10, 20, 30, 40, 50)

first_el = my_tuple[0]
second_el = my_tuple[1]
third_el = my_tuple[2]
last_el = my_tuple[-1]

print(first_el)
print(second_el)
print(third_el)
print(last_el)

# count()
_tuple = (1, 2, 3, 2, 4, 2, 5)
count_of_2 = _tuple.count(2)
print('Count of 2 in the tuple: ', count_of_2)

# index()
index_of_2 = _tuple.index(2)
print('index of first 2:', index_of_2)
print('index of 3:', _tuple.index(3))

# Розрізи (Slices)

sub_tuple = _tuple[::2]
print('full tuple', _tuple)
print('sub tuple', sub_tuple)

# Розпакування (Unboxing)

a, b, c = (10, 20, 30)

print(a)
print(b)
print(c)

# формування кортежів з інших типів даних
my_str = "Привіт, світ!"
tuple_from_str = tuple(my_str)

print(tuple_from_str)

my_list = [1, 2, 3.14, 'Python', True]

tuple_from_list = tuple(my_list)
print(tuple_from_list)