class Dog:
    def make_sound(self):
        return "Woof!"


class Cat:
    def make_sound(self):
        return "Meow!"


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass


class Dogs(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        return "Woof!"


class Cats(Animal):
    """
    Class Cats for creating cats objects with custom name and method 'make_sound' that returns 'Meow!'
    """

    def make_sound(self):
        return "Meow!"


if __name__ == "__main__":
    animals = [Cat(), Dog()]
    for animal in animals:
        print(animal.make_sound())

    animals = [Dogs("Buddy"), Cats("Whiskers"), Dog(), Cat()]

    for animal in animals:
        if isinstance(animal, Animal):
            print(f"{animal.name} says: {animal.make_sound()}")
        else:
            print(animal.make_sound())
