class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        print(f"The {self.make} {self.model} object has been destroyed.")


# Class object creation
my_car = Car("Toyota", "Camry")

# Utilization
print(my_car)
print(my_car.make, my_car.model)
my_car.model = "Highlander"
print(my_car.make, my_car.model)

# del - Delete object
del my_car
# print(my_car)

a = print
a("Hello")

print(a)

del a

# print(a)


# FileHandler


class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        print(f"File {self.filename} has been open")

    def read_data(self):
        print(f"File {self.filename} has been read")
        return self.file.read()

    def __del__(self):
        self.file.close()
        print(f"File {self.filename} has been closed")


file_handler = FileHandler("example.txt", "r")
data = file_handler.read_data()
del file_handler
