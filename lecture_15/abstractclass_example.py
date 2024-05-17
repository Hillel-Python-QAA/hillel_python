from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def breed(self):
        return 'Animal'


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Woof!'

    def breed(self):
        return 'Beagle'


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Meow!'


def introduce(animal):
    print(f'My name is {animal.name} and I say {animal.make_sound()} and I\'m a(an) {animal.breed()}')


dog = Dog('Oscar')
cat = Cat('Kitty')

introduce(dog)
introduce(cat)


class Bird(Animal):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Tweet!'


bird = Bird('Sparrow')
introduce(bird)


class Simple:
    @abstractmethod
    def abcmethod(self):
        raise NotImplementedError


class Inherited(Simple):
    pass


Inherited().abcmethod()
