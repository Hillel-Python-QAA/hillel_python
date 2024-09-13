class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        pass


class Mammal(Animal):
    def __init__(self, name, num_legs):
        Animal.__init__(self, name)
        self.num_legs = num_legs


class Bird(Animal):
    def __init__(self, name, wingspan):
        Animal.__init__(self, name=name)
        self.wingspan = wingspan


class Bat(Mammal, Bird):
    def __init__(self, name, num_legs, wingspan):
        Mammal.__init__(self, name=name, num_legs=num_legs)
        Bird.__init__(self, name=name, wingspan=wingspan)

    def sound(self):
        return "Squeak"


bat = Bat("Bat", 2, 30)

print("Name:", bat.name)
print("Num Legs:", bat.num_legs)
print("Wingspan:", bat.wingspan)

print("Sound:", bat.sound())

print(Bat.mro())

#                Animal
#                /    \
#             Mammal  Bird
#                \    /
#                  Bat
