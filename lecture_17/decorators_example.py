def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


def say_hello2():
    print("Hello!")


decorated_funct = my_decorator(say_hello2)
decorated_funct()

say_hello()
say_hello2()


def my_decorator2(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator2
def say_hello(name):
    print(f"Hello, {name}!")


say_hello("Siri")


def setup_teardown_decorator(func):
    def wrapper(*args, **kwargs):
        setup()
        result = func(*args, **kwargs)
        teardown()
        return result

    return wrapper


@setup_teardown_decorator
def test_example():
    # Тут проводяться тести
    pass


from datetime import datetime


def my_decorator3(func):
    def wrapper():
        print("start of the decorator")
        func()
        print("end of the decorator")

    return wrapper


@my_decorator3
def say_yuppi():
    print("Yuppi!")


# say_yuppi()


# say_yuppi = my_decorator(say_yuppi) # variant without decorator


def not_during_the_night(func):
    def wrapper():
        if 7 >= datetime.now().hour >= 22:
            func()
        else:
            print("Tsss!!!")

    return wrapper


def do_twise(func):
    def wrapper():
        func()
        func()

    return wrapper


@my_decorator3
@not_during_the_night
@do_twise
def say_yuppi():
    print("Yuppi!")


say_yuppi()


class MyClass:
    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

    @staticmethod
    def my_static_method():
        print("This is a static method.")

    @classmethod
    def my_class_method(cls):
        print("This is a class method.")


my_cls = MyClass(5)

print(my_cls.x)
my_cls.my_static_method()
MyClass.my_static_method()
my_cls.my_class_method()
MyClass.my_class_method()
