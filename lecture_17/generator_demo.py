def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()
print(fib)
for _ in range(10):
    print(next(fib))

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

square_gen = (x**2 for x in range(10))
print(square_gen)

for square in square_gen:
    print(square)

# yield


def simple_gen():
    yield "one"
    yield "two"
    yield "three"


simple_g = simple_gen()

print(next(simple_g))
print(next(simple_g))
print(next(simple_g))


def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1


counter = count_up_to(10)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
