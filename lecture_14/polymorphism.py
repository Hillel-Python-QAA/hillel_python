class Dog:
    def make_sound(self):
        return 'Woof!'


class Cat:
    def make_sound(self):
        return 'Meow!'


animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dogs(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return 'Woof!'


class Cats(Animal):
    def make_sound(self):
        return 'Meow!'


animals = [Dogs('Buddy'), Cats('Whiskers'), Dog(), Cat()]

for animal in animals:
    if isinstance(animal, Animal):
        print(f'{animal.name} says: {animal.make_sound()}')
    else:
        print(animal.make_sound())
