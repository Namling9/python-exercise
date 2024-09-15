'''Object-Oriented Programming (OOP) in Python is a programming paradigm that uses objects
and classes to structure and organize code. 
OOP is based on the concept of "objects," 
which can represent real-world entities or abstract concepts, and "classes," 
which define the blueprint or template for these objects.'''


# Class

'''A class is a blueprint for creating objects. 
It defines a set of attributes (variables) and methods (functions) that 
the objects created from the class will have.'''

'''
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")
        
# Object

An object is an instance of a class. When a class is defined,
no memory is allocated until an object of that class is created.

my_dog = Dog("Buddy", "Golden Retriever") 
my_dog.bark()  # Output: Buddy says woof!

print(my_dog.name) #Buddy 
'''

'''
class Employee:
    def __init__(self): # Dunder function/method (It will be called whenever new object is created)
        
        print("Hello This is an object created using dunder method")
        
        
    language = "py" # Class attribute
    salary = 1200000
    
    def getinfo(self):
        
        print(f"{self.name}'s language is {self.language} and salary : {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")
        
harry = Employee()
harry.name = "Harry" # Instance Attribute
print(harry.name , harry.salary, harry.language) #Harry 1200000 py

rohan = Employee()
rohan.name = "Rohan" # Instance Attribute
print(rohan.name, rohan.salary, rohan.language) #Rohan 1200000 py

rohan.language = "Java" # Instance attribute(variable)
print(rohan.language) #Java (Because Instance attribute is prefered over class attribute during assignment & retrieval)

harry.getinfo() # runs like this Employee.getinfo(harry) that's why we use self parameter/arguement in function of class.
#Harry's language is py and salary : 1200000

harry.greet()

'''
#Constructor
''' a constructor is a special method that is automatically called when an object of a class is created. 
The purpose of the constructor is to initialize the object's attributes
with the values passed to it during the creation of the object.'''
# __intit__ method
class Employee:
    def __init__(self,name,salary,language): # Dunder function/method (It will be called whenever new object is created)
        
        self.name = name
        self.salary = salary
        self.language = language
        
        

harry = Employee("Harry",1300000,"Python")
print(harry.name,harry.salary,harry.language) #Harry 1300000 Python
        

