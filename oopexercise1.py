'''1. Create a class “Programmer” for storing information of few programmers 
working at Microsoft.'''
'''import math
class programmer:
    company = "Microsoft"
    def __init__(self,name,language,department,salary):
        
        self.name = name
        self.language = language
        self.department = department
        self.salary = salary 
    

namling = programmer("Namling Limbu", "Python", "AI / Data Science", "500000$")
print(namling.name,namling.language,namling.department,namling.salary) '''
        
'''2. Write a class “Calculator” capable of finding square, cube and square root of a 
number.'''
'''
import math
class Calculator:
    
    def __init__(self,number):
        self.number = number
        
    def find_square(self):
        print("Square : ",self.number*self.number)
    
    def find_cube(self):
        print("Cube: ", self.number*self.number*self.number)
    
    def find_squareroot(self):
        print("Square Root: ", math.sqrt(self.number))
    
    

result = Calculator(9)
result.find_square()
result.find_cube()
result.find_squareroot() '''

        
'''3. Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?'''

class value:
    
    a = None
    

object = value()
object.a = 5
print(object.a) # Five

object2 = value()
print(object2.a) # None

#4. Add a static method in problem 2, to greet the user with hello
import math
class Calculator:
    
        
    def find_square(self, number):
        print("Square : ",number*number)
    
    def find_cube(self,number):
        print("Cube: ", number*number*number)
    
    def find_squareroot(self,number):
        print("Square Root: ", math.sqrt(number))
    
    @staticmethod
    def greet():
        print("Hello, Goodmorning")

result = Calculator()
result.find_square(9)
result.find_cube(9)
result.find_squareroot(9) 
result.greet()

'''5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
and get fare information of train running under Indian Railways.
'''
from random import randint
class train:
    
    def __init__(self, TrainNo, fro, to):
        
        self.TrainNo = TrainNo
        self.fro = fro
        self.to = to
        
    def book(self):
        print(f"\n Ticket is booked in train number: {self.TrainNo}\n From : {self.fro} \n Destination: {self.to} \n \n ")
        pass
    
    def get_status(self):
        print(f"Train number : {self.TrainNo} is running on time. \n \n")
    
    def get_fare(self):
        
        print(f"Train Number : {self.TrainNo} \n From : {self.fro} \n Destination : {self.to} \n \n")
        
    
customer1 = train(12323,"kerela", "Bangolure")
customer1.book()
customer1.get_status()
customer1.get_fare()