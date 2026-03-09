#OOPS stands for Object Oriented Programming System.
#It's a  programming style where we organize code using objects and classes instead of just functions and variables.
#A class is a blueprint or template for creating objects.
#An object is an instance of a class.
#Constructor is a special method that runs automatically when an object is created.
#It's main job is to initialize object's data.
#self keyword refer to the current object.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary
    
ayush = Employee("Ayush", 10000000)
print(ayush.salary)
print(ayush.name)

rahul = Employee("Rahul", 50000)
print(rahul.salary)
print(rahul.name)