# local variable x with the scope of function
def example_func():
    x = 10
    print(x)


example_func()

# global

y = 20

print(y)


def another_func():
    print(y)


another_func()


# nonlocal


def outer_func():
    z = 30

    def inner_func():
        print(z)

    inner_func()


outer_func()


## LEGB - Local Enclosing Global Built-in
# - у локальній області видимості всередині функції (Local);
# - у локальних областях видимості охоплюючих функцій (Enclosing);
# - у глобальній області видимості (Global);
# - у вбудованій області видимості (Built-in).


# Recursion
def factorial(x):
    if x in [0, 1]:
        return 1
    return x * factorial(x - 1)


print(factorial(19))

# global, nonlocal - special words
global_var = None


def global_example():
    global global_var
    global_var = 150


global_example()

print(global_var)


def top_func():
    # global x
    x = None
    print('top', x)

    def nested_func():
        # global x
        nonlocal x
        print(x)
        x = 5
        print('nested', x)

    nested_func()
    print('top', x)


top_func()
