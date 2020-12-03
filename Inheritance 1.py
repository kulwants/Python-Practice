class Pet:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I dont know what to speak")
        
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
        
    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} in color.")
        
class Dog(Pet):
    def speak(self):
        print("Bark")


p = Pet("Boo", 19)
p.show()
p.speak()       ## Speaks out the defined attribute
c = Cat("Pee", 29, "Black")
c.show()
c.speak()       ## Speaks out the defined attribute
d = Dog("Zee", 25)
d.show()
d.speak()       ## Speaks out the defined attribute
