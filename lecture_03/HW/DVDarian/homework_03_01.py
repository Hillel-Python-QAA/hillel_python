alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."\n'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
total_area = black_sea_area + azov_sea_area
print(f'Чорне та Азовське моря разом займають площу {total_area} км2.\n')



# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_amount_of_goods = 375291
warehouse1_warehouse2_amount = 250449
warehouse2_warehouse3_amount = 222950
warehouse1_amount = total_amount_of_goods - warehouse2_warehouse3_amount
warehouse2_amount = warehouse1_warehouse2_amount - warehouse1_amount
warehouse3_amount = warehouse2_warehouse3_amount - warehouse2_amount
print(f'На першому складі розміщено {warehouse1_amount} товарів.\n'
      f'На другому складі розміщено {warehouse2_amount} товарів.\n'
      f'На третьому складі розміщено {warehouse3_amount} товарів.\n')


# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
paid_period = 18
monthly_payment = 1179
computer_cost = paid_period * monthly_payment
print(f'Вартість комп’ютера становить {computer_cost} грн.\n')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
a = 8019 % 8
b = 9907 % 9
c = 2789 % 5
d = 7248 % 6
e = 7128 % 5
f = 19224 % 9
print(f'Oстачa від діленя чисел:\n'
      f'a) 8019 : 8 становить {a}     d) 7248 : 6 становить {d}\n'
      f'b) 9907 : 9 становить {b}     e) 7128 : 5 становить {e}\n'
      f'c) 2789 : 5 становить {c}     f) 19224 : 9 становить {f}\n')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
big_pizzas = 4 * 274
middle_pizzas = 2 * 218
juice = 4 * 35
cake = 350
water = 3 * 21
total_cost = big_pizzas + middle_pizzas + juice + cake + water
print(f'Для замовлення Іринки знадобиться {total_cost} грн.\n')


# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_amount_of_photos = 232
amount_of_photos_per_page = 8
amount_of_pages = total_amount_of_photos // amount_of_photos_per_page
print(f'Ігорю знадобиться {amount_of_pages} сторінок, щоб вклеїти всі свої фото.\n')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
total_distance = 1600
petrol_per_100_km = 9
tank_capacity = 48
total_distance_petrol = total_distance * petrol_per_100_km // 100
fill_tank_amount = total_distance_petrol // tank_capacity
print(f'1) Для подорожі із Харкова в Будапешт знадобиться {total_distance_petrol} літрів бензину.\n'
      f'2) Родині необхідно заїхати на заправку під час цієї подорожі {fill_tank_amount} рази,\n'
      f'кожного разу заправляючи повний бак.')
