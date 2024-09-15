# Single level inheritance

# class student:
#     name = input("Enter your name : ")
#     room = int(input("Enter your Classroom number: "))
#     Semester = int(input("Enter your semester: "))
#     faculty = input("Enter your faculty: ")

#     def details(self):
        
#         print(f'''
#               Name : {self.name}
#               Classroom : {self.room}
#               Semester: {self.Semester}
#               Faculty : {self.faculty}''')
    
# class result(student):
    
#     def marks(self):
#         print(f'''
#               Name : {self.name}, Faculty: {self.faculty}, Semester: {self.Semester}
              
#               Math : 99
#               Science : 98
#               English : 97
#               Computer : 99
#               Social : 96
#               ''')
        
# student1 = result()
# student1.details()
# student1.marks()


# Multiple Inheritance
'''
class Employee:
    
    company = "ICT"
    name = "ram"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class coder:
    
    language = "Python"
    
    def printlanguages(self):
        print(f"The language used by the employee is {self.language}")
        

class programmer(Employee, coder):
    company = "ICT Infotech"
    
    def showlanguage(self):
        print(f"The company name is {self.company} and He is good with language: {self.language}")
    

programmer1 = programmer()

print(programmer1.company)

programmer1.show() #The name of the employee is ram and the company is ICT Infotech
programmer1.printlanguages() # The language used by the employee is Python
programmer1.showlanguage() #The company name is ICT Infotech and He is good with language: Python

'''

# Multilevel Inheritance
'''class Employee():
    a =1

class programmer(Employee):
    b =2 

class manager(programmer):
    c =3
    

manager1 = manager()
print(manager1.a, manager1.b, manager1.c) #1 2 3

programmer1 = programmer()
print(programmer1.a,programmer1.b) #1 2

employee1 = Employee()
print(employee1.a) #1
'''


# super() method 
'''
class Employee:
    a =1
    def  __init__(self):
        print("This is Employee constructor")
       

class programmer(Employee):
    b =2 
    def __init__(self):
        print("This is programmer constructor")
       

class manager(programmer):
    c =3
    def __init__(self):
        super().__init__()
        print("This is manager constructor")
       
'''

# manager1 = manager()
# print(manager1.a, manager1.b, manager1.c) 
# '''This is programmer constructor 
#    This is manager constructor
#    1 2 3'''
# programmer1 = programmer()
# print(programmer1.a,programmer1.b) 
# '''
# This is programmer constructor
# 1 2'''

# employee1 = Employee()
# print(employee1.a) 
# '''This is Employee constructor
#    1
# '''

# class method
'''
class employee : 
     a =1 
     @classmethod
     def show(cls):
         
        print("This is an 'a':", cls.a )


employee1 = employee()
employee1.a = 45
employee1.show() # This is an 'a': 1 (Because this method is under @classmethod)

'''

# Property decorator
class employee : 
     a =1 
     @classmethod
     def show(cls):
         
        print("This is an 'a':", cls.a )
     
     @property
     def name(self):
         return f"{self.fname} {self.lname}"
     
     @name.setter
     def name(self, value):
         self.fname = value.split()[0]
         self.lname = value.split()[1]
     
         

e = employee()

e.name = "Harry Khan"
print(e.name, e.fname)
