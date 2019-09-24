class Organism:
    def __init__(self):
        print("Calling Organism.__init__")


class Animal(Organism):
    def __init__(self):
        print("Calling Animal.__init__")
        super().__init__()


class Herbivore(Animal):
    pass


class Carnivore(Animal):
    pass


class Sheep(Herbivore):
    pass


class Wolf(Carnivore):
    pass


if __name__ == "__main__":
    dolly = Sheep()
    print(isinstance(dolly, Animal))
