# Class declaration
# class Car:
#     pass


# Class's object
# car = Car()


class Car:
    def __init__(self, brand, model, year_of_production):
        self.brand = brand
        self.model = model
        self.year_of_production = year_of_production


prius_car = Car("Toyota", "Prius", "2015")

print(prius_car)
print(isinstance(prius_car, Car))
print(prius_car.model)
print(prius_car.brand)
print(prius_car.year_of_production)

prius_car.year_of_production = 2020
print(prius_car.year_of_production)

i = 4


# OOP


class Fruit:
    def __init__(self, color):
        self.color = color


apple = Fruit("green")

orange = Fruit("orange")

cherry = Fruit("red")

print(isinstance(apple, Fruit))
print(isinstance(orange, Fruit))

fruit_list = [apple, orange, cherry]

for fruit in fruit_list:
    if fruit.color == "green":
        print("This is apple")
    elif fruit.color == "orange":
        print("This is orange")
    else:
        print("This fruit is not recognized: {}".format(fruit.color))


# Інкапсуляція


# Class Private access with double underscore '__balance'
# Class Protected access with single underscore '_currency'
class BankAccount:
    _account_number = 1234

    def __init__(self, initial_balance, currency):
        self.__balance = initial_balance
        self._currency = currency

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        if type(value) not in [int, float]:
            raise TypeError("Value type {} is not acceptable.".format(type(value)))
        self.__balance = value

    def __str__(self):
        return f"Balance: {self.__balance} {self._currency}"

    def __eq__(self, other):
        return self.__balance == other.__balance and self._currency == other._currency


account = BankAccount(1000, "USD")
account.account_number = 128437978234657946597834
print(account.account_number)
other_account = BankAccount("1000", "USD")
other_account.account_number = 87465734658734658734678
print(other_account.account_number)
print(account._account_number)
print(BankAccount._account_number)

print("Equality:", account.__eq__(other_account))

print(account.get_balance())
print(account._currency)
# print(account.__balance)

account.set_balance(2000)
print(account.get_balance())

print(str(account))
