greetings = "Whazzup"

match greetings.lower():
    case "hello" | "hi" | "whazzup":
        print("Hi, there")
    case _:  # Default
        print("Don't be so rude!")


x, y, z = 4, 19, 2
match (x, y, z):
    case 4, 19, int() as z if z % 2 != 0:
        print("z is odd, the value of x is 4 and y is 19")
    case 4, _, _:
        print("the value of x is 4")
    case _, 19, _:
        print("the value of y is 19")
