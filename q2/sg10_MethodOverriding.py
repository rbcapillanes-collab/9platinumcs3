class Animal: # creates the parent class: Animal
    def __init__(self, name: str): # creates the properties of the class
        self._name = name

    def eat(self): # creates the methods of the class
        print(f"{self._name} eats food.") # calls the name of the animal and says they eat food 
    def make_sound(self, name): 
        print(f"{self._name} makes a sound.") # calls the name of the animal and says they make sounds 

class Lion(Animal): # 1st child class of the parent class, Animal 
    def __init__(self, name: str): # makes Animal a superclass and makes it so that Lion is its child class
        super().__init__(name) 

    def eat(self): # Overrides the eat method, Animal, class. Instead of it saying "{animal} eats food." it changes it to "{animal} eats fresh meat"
        print(f"{self._name} eats fresh meat.")
    def make_sound(self): # Overrides the make_sound method from the parent, Animal, class. Instead of it saying "{animal} makes a sound" it changes it to "{animal} roars loudly!" 
        print(f"{self._name} roars loudly!")

class Elephant(Animal): # 2nd child class of the parent class, Animal
    def __init__(self, name: str): #makes Animal a superclass (parent class) and makes it so that Elephant is its child class
        super().__init__(name)

    def eat(self): # Overrides the eat method, Animal, class. Making it say "{Animal} eats grass and fruits." 
        print(f"{self._name} eats grass and fruits.")
    def make_sound(self): # Overrides the make_sound method, Animal, class. Making it say "{Animal} trumpets." 
        print(f"{self._name} trumpets.")

class Monkey(Animal):
    def __init__(self, name: str): 
        super().__init__(name)

    def eat(self):  # Overrides the eat method, Animal, class. Making it say "{Animal} eats bananas."
        print(f"{self._name} eats bananas.") 
    def make_sound(self):  # Overrides the make_sound method, Animal, class. Making it say "{Animal} chatters." 
        print(f"{self._name} chatters.")

lion = Lion("Simba") # creates an object from the lion class named Simba
elephant = Elephant("Dumbo") # creates an object from the elephant class named Dumbo
monkey = Monkey("George") # creates an object from the monkey class named george 

lion.make_sound() # calls the sound and food the lion makes and eats 
lion.eat()
print("-----")

elephant.make_sound() # calls the sound and food the elephant makes and eats 
elephant.eat()
print("-----")

monkey.make_sound() # calls the sound and food the monkey makes and eats 
elephant.eat()
print("-----")





