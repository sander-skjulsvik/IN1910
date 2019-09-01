def my_decorator(f):
    def wrapper():
        print("Hello before function call")
        f()
        print("Hello after function call")

    return wrapper


def say_hello():
    print("Hello")


@my_decorator
def say_hello_decorated():
    print("Hello")


if __name__ == "__main__":

    print("\nCalling say_hello()")
    say_hello()

    print("\nCalling say_hello_decorated()")
    say_hello_decorated()

    say_hello2 = my_decorator(say_hello)
    print("\nCalling my_decorator(say_hello)()")
    say_hello2()

