def divide(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError as ex:
        print(f"{ex} occurred, please try again")
        b = float(input("please input any number except 0:"))
        result = a / b
    except TypeError as tr:
        print('TypeError', tr)
    except Exception as e:
        print('Exception', e)
    finally:
        return result


def try_except(a, b):
    try:
        return a/b
    except Exception as e:
        print(f"{e}: error occurred in try-except block")


def try_finally(a, b):
    result = None
    try:
        result = a/b
    finally:
        print("try-finally example")
        return result


def try_excepts_finally(a, b):
    result = None
    try:
        result = a / b
    except ZeroDivisionError as ex:
        print(f"{ex} occurred, please try again")
        b = float(input("please input any number except 0:"))
        result = a / b
    except TypeError as tr:
        print('TypeError', tr)
    except Exception as e:
        print('Exception', e)
    finally:
        return result


def try_except_else(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    else:
        print(f"Result of division {a} by {b}: {result}")


def try_except_else_finally(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
    else:
        print(f"Result of division {a} by {b}: {result}")
    finally:
        print("Finally is always printed")


def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")


class TooLargeValueError(Exception):
    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        message = f'Value {value} are greater then the limit {limit}'
        super().__init__(message)


if __name__ == "__main__":
    print(divide(4, 2))  # 2.0
    print(divide(2, 4))  # 0.5
   # print(divide(2, 0))  # ZeroDivisionError
    print(divide(2, 'a'))  # ZeroDivisionError

    try_except_else(4, 0)
    try_except_else(4, 1)

    try_except_else_finally(4, 0)
    try_except_else_finally(4, 1)

    try:
        user_age = int(input("Enter your age: "))
        check_age(user_age)
        print(f"Your age: {user_age}")
    except ValueError as ve:
        print(f"Error: {ve}")


    try:
        limit = 100
        user_input = int(input("Enter number: "))
        if user_input > limit:
            raise TooLargeValueError(user_input, limit)
        else:
            print("Thank you! You have enter the number within the limit!")
    except TooLargeValueError as e:
        print(f"Error: {e}")
    except ValueError:
        print("Error: Please enter an integer number")



