class Rabbit1:
    nr_of_rabbits = 0

    def __init__(self, age):
        # Variable is stored on the class (not self)
        Rabbit1.nr_of_rabbits += 1
        self.age = age


def test_rabbit1():
    print(Rabbit1.nr_of_rabbits)

    alice = Rabbit1(2)
    buddy = Rabbit1(4)
    charlie = Rabbit1(7)

    print(Rabbit1.nr_of_rabbits)
    print(alice.nr_of_rabbits)

    alice.nr_of_rabbits = 1

    print(Rabbit1.nr_of_rabbits)
    print(alice.nr_of_rabbits)


class Rabbit2:
    all_rabbits = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # This works because lists are mutable
        # self.all_rabbits.append(self)

        # But this it better because it shows the user
        # that you are using a class variable
        Rabbit2.all_rabbits.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name})"


def test_rabbit2():

    alice = Rabbit2("Alice", 2)
    buddy = Rabbit2("Buddy", 4)
    charlie = Rabbit2("Charlie", 7)
    print(Rabbit2.all_rabbits)
    print(charlie.all_rabbits)


class Pendulum:
    G = 9.81

    def __init__(self, M=1, L=1):
        self.M = M
        self.L = L


def test_pendulum():
    p = Pendulum(M=4, L=2)
    print(p.M)
    print(p.L)
    print(p.G)


if __name__ == "__main__":
    test_rabbit1()
    test_rabbit2()
