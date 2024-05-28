from datetime import datetime, date
import time

# fromordinal()
ordinal_day = 739034
dt = datetime.fromordinal(ordinal_day)
print(ordinal_day)
print(dt)

# toordinal()
today_ = datetime.today()
print(today_)
print(datetime.toordinal(today_))


def day_of_year(date_str):
    # Перетворення рядка у об'єкт datetime
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')

    # time
    time_obj = time.strptime(date_str, '%Y-%m-%d').tm_yday
    print('Time year day:', time_obj)

    # Отримання порядкового номера дня
    day_number_ = date_obj.toordinal() - datetime(date_obj.year, 1, 1).toordinal() + 1

    return day_number_


# Приклад виклику функції
date_str = '2024-05-28'
day_number = day_of_year(date_str)
print(f'Порядковий номер дня для {date_str}: {day_number}')

# fromtimestamp
# Приклад мітки часу (timestamp)
timestamp = 1634545800  # UNIX Epoch: 18 жовтня 2021 року 10:30:00 UTC

# Створення об'єкта datetime з мітки часу
dt = datetime.fromtimestamp(timestamp)
print(time.mktime(datetime.strptime("2021-10-18 10:30:00", "%Y-%m-%d %H:%M:%S").timetuple()))

print(dt)
# Виведе: 2021-10-18 10:30:00

# today
print(date.today())

# now

print(datetime.now())
print(datetime.today())

# ctime
print(dt.ctime())

# isoformat
print(dt.isoformat())

# replace
print(dt.replace(year=2023, day=24))

# weekday
print(dt.weekday())
