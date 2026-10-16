# Parent class (Base class)
class Animal:
<<<<<<< HEAD

=======
    
>>>>>>> upstream/main
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True
<<<<<<< HEAD

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

=======
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")
    
>>>>>>> upstream/main
    def make_sound(self):
        print(f"{self.name} makes a sound")

# Child class (Derived class)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")  # Call parent constructor
        self.breed = breed
<<<<<<< HEAD

    # Method overriding
    # Method overriding รับถ่ายทอดจากแม่
    def make_sound(self):
        print(f"{self.name} barks: Woof!")

=======
    
    # Method overriding
    def make_sound(self):
        print(f"{self.name} barks: Woof!")
    
>>>>>>> upstream/main
    # New method specific to Dog
    def fetch(self):
        print(f"{self.name} is fetching the ball")

class Cat(Animal):
<<<<<<< HEAD

    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color

    def make_sound(self):
        print(f"{self.name} meows: Meow!")

=======
    
    def __init__(self, name, color):
        super().__init__(name, "Feline")
        self.color = color
    
    def make_sound(self):
        print(f"{self.name} meows: Meow!")
    
>>>>>>> upstream/main
    def climb_tree(self):
        print(f"{self.name} is climbing a tree")

# Usage
dog = Dog("Max", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

dog.eat()        # Inherited method
dog.make_sound() # Overridden method
dog.fetch()      # Dog-specific method

<<<<<<< HEAD
cat.make_sound() # Overridden method
=======
cat.make_sound() # Overridden method
cat.climb_tree() # Cat-specific method
>>>>>>> upstream/main
