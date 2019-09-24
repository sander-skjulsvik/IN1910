class Organism:
    pass


class Animal(Organism):
    pass


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
