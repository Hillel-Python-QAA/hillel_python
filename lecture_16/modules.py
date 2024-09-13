import sys
import lecture_14.polymorphism as pm


cat = pm.Cats("Barsik")

print(cat.name, cat.make_sound())

# help(sys)
print(dir(sys))

print(dir(pm))

print(pm.__name__)
print(pm.__package__)
print(pm.__spec__)
print(pm.__file__)
print(pm.__doc__)
print(sys.__doc__)

print(dir(cat))
print(dir(pm.Cats))
