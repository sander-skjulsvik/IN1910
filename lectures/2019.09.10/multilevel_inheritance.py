class Organism:
    def __init__(self):
        print('Calling Organism __init__')


class Animal(Organism):
    def __init__(self):
        print("Calling Animal __init__")

    def method(self):
        print("calling method animal")


class Herbivore(Animal):
    def __init__(self):
        print("Calling Herbivore __init__")

    def method(self):
        print("calling method in Herbivore")



class Carnivore(Animal):
    pass


class Sheep(Herbivore):
    def method(self):
        print("calling method in sheep")
        # Animal.method(self)
        super().method()


class Wolf(Carnivore):
    pass


if __name__ == "__main__":
    # # o = Organism()
    # animal = Animal()
    dolly = Sheep()
    dolly.method()
