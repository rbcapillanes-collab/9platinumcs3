class Animal:
    def __init__(self, name: str):
        self._name = name

    def eat(self):
        print(f"{self._name}, eats food.")
    def make_sound(self, name):
        print(f"{self._name} makes sounds.")

class Lion(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def eat(self):
        print(f"{self._name} eats fresh meat.")
    def make_sound(self):
        print(f"{self._name} roars loudly!")

class Elephant(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def eat(self):
        print(f"{self._name} eats grass and fruits.")
    def make_sound(self):
        print(f"{self._name} trumpets! ")

class Monkey(Animal):
    def __init__(self, name: str):
        super().__init__(name)

    def eat(self):
        print(f"{self._name} eats bananas.")
    def make_sound(self):
        print(f"{self._name} chatters!")

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

lion.make_sound()
lion.eat()
print("-----")

elephant.make_sound()
elephant.eat()
print("-----")

monkey.make_sound()
elephant.eat()
print("-----")





