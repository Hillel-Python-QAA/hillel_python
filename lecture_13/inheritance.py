class Animal:
    def birth(self):
        print('This animal has births')

    def speak(self):
        pass


class Dog(Animal):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def speak(self):
        return 'Wow'


class Cat(Animal):
    def speak(self):
        return 'Meow'


dog = Dog('Oscar', 'Beagle')
cat = Cat()

dog.birth()
cat.birth()

print(dog.speak())
print(cat.speak())


class Mammal:
    def __init__(self, breed, paws):
        self.breed = breed
        self.paws = paws


class Dolphin(Mammal, Animal):
    def __init__(self, name, breed, paws):
        super().__init__(breed, paws)
        self.name = name

    def speak(self):
        return 'hello'


dolphin = Dolphin(name='Flipper', breed='dolphin', paws=0)

print(dolphin)
print(dolphin.name)
print(dolphin.breed)
print(dolphin.paws)
dolphin.birth()
print(dolphin.speak())


print(isinstance(dolphin, Dolphin))
print(isinstance(dolphin, Animal))
print(isinstance(dolphin, Mammal))
print(isinstance(dolphin, object))
print(type(dolphin))

print(Dolphin.mro())

# Polymorphism


def make_sound(animal):
    return animal.speak()


print(make_sound(dog))
print(make_sound(cat))
print(make_sound(dolphin))
