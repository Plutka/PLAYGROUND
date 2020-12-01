from my_math import add_numbers
from person import Person

name = "Ada"
name2 = "Maria"


def hello(name_user: str):
    print('Hello ' + name_user.upper())


def hello2(name_user: str):
    print('Hello ' + name_user.upper())


def alex_method(name_met):
    p = Person(name_met)
    print(p)


if __name__ == '__main__':
    # TODO: Fix Bug
    # TODO: Implement Tests
    print("Pycharm is awesome")
    print("natalia")
    print("Hello world")
    print("Hello")
    natalia = "NATALIA"
    print(natalia)
    hello(name)
    print(add_numbers(2, 3))

    alex_method("Ali")
