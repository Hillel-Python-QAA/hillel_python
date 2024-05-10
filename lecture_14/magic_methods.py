# __init__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person('John', 25)
print(person.name, person.age)
print(person)


# __str__
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


book = Book('The Great Gatsby', 'F. Scott Fitzgerald')
print(book.title, book.author)
print(book)


# __len__
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def __len__(self):
        return len(self.__items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(0)
print(len(stack))


# __add__

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other_point):
        return Point(self.x + other_point.x, self.y + other_point.y)


point1 = Point(1, 2)
point2 = Point(3, -4)

result = point1 + point2
result1 = point1.__add__(point2)
print(result.x, result.y)
print(result1.x, result1.y)


# __eq__

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other_circle):
        return self.radius == other_circle.radius


circle1 = Circle(5)
circle2 = Circle(5)
circle3 = Circle(3)

print(circle1 == circle2)  # True
print(circle1 == circle3)  # False
