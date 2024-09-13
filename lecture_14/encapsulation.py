class Car:
    def __init__(self, make, model):
        self.make = make  # public
        self._model = model  # protected
        self.__year = 2024  # private

    def display_model(self):
        print(f"Model: {self._model}")

    def display_year(self):
        print(f"Year: {self.__year}")

    def update_year(self, new_year):
        self.__year = new_year


my_car = Car("BMW", "X7")
print(my_car.make)
my_car.display_year()
my_car.display_model()
my_car.update_year(2023)
my_car.display_year()


class Toyota(Car):
    def __init__(self, model, make="Toyota", engine_type="Petrol"):
        Car.__init__(self, make, model)
        self.engine_type = engine_type

    def change_model(self, new_model):
        self._model = new_model


toyota = Toyota("Toyota", "Prius", "Hybrid")

toyota.display_year()
toyota.update_year(2005)
toyota.display_year()

toyota2 = Toyota("Toyota", "Camry")
print(toyota2.engine_type)
toyota2.display_model()

toyota3 = Toyota("Corolla")

print(toyota3.engine_type)
toyota3.display_model()
