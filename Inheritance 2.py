class Person:
    number_of_people = 0
    def __init__(self, name, employee_id, age, access):
        self.name           = name
        self.employee_id    = employee_id
        self.age            = age
        self.access         = access
        Person.number_of_people += 1

    def show(self):
        print(f"I am {self.name}.")
        print(f"My Employee ID is {self.employee_id}.")
        print(f"I am {self.age} years old.")

    def speak(self):
        print(f"I have access as a {self.access}.")
        print()
        
class Manager(Person):        
    def show(self):
        print(f"I am {self.name}. My Employee ID is {self.employee_id}. I am {self.age} years old. I have Access of Manager.")
        
class Employee(Person):
    def show(self):
        print(f"I am {self.name}. My Employee ID is {self.employee_id}. I am {self.age} years old. I have Access of Employee.")

p1 = Person("Asphalt", 1101, 25, "Manager")
print(Person.number_of_people)
p1.show()
p1.speak()
p2 = Person("Bob", 1102, 27, "Employee")
print(Person.number_of_people)
p2.show()
p2.speak()
p3 = Person("Charlotte", 1103, 31, "Manager")
print(Person.number_of_people)
p3.show()
p3.speak()
p4 = Person("Daniel", 1104, 24, "Employee")
print(Person.number_of_people)
p4.show()
p4.speak()





