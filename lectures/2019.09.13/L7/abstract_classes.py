from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

    def make_sound(self):
        print(f"{self.__class__.__name__} {self.name} sais {self.sound()}")


class Dog(Animal):
    def sound(self):
        return "Voff"


class Cat(Animal):
    pass


if __name__ == "__main__":
    fido = Dog("Fido")
    fido.make_sound()

    jess = Cat("Jess")
