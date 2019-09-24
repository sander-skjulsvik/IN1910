

class Rabbit:

    all_rabbits = []

    def __init__(self, name):
        self.name = name

        Rabbit.all_rabbits.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

if __name__ == "__main__":
    r1 = Rabbit("Alice")
    r2 = Rabbit("Bob")
    r3 = Rabbit('Eve')

    print('r1')
    print('r2')

    print(r1.all_rabbits)

    # r1.all_rabbits = []
    print(r2.all_rabbits)