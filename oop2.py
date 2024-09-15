# del keyword (it deletes the whole object or properties of class )

# class student:
    
#     def __init__(self,name):
        
#         self.name = name
    
#     def print_name(self):
#         print(f"My name is {self.name}")

# s1 = student("Namling")
# s1.print_name() #My name is Namling
# del s1 # Delete the s1 object of the class student
# print(s1) #error
# s1.print_name() #error

# Private access modifier

# class account:
    
#     def __init__(self, accountNumber, accountPassword):
        
#         self.accountNumber = accountNumber
#         self.__accountPassword = accountPassword #Private variable ( __ infront of makes variable private)
        
#     def print_details(self):
        
#         print(f''' 
#               Account Number : {self.accountNumber}
#               Account Password: {self.__accountPassword}''')
        

# a1 = account(1294223, "Banana")
# print(a1.accountNumber)
# #print(a1.__accountPassword) # Cannot exccess like this (Shows error)
# a1.print_details()

class person : 
    
    __name = "anonymous"
    
    def __hello():
        print("HEllo person")
        
    
    def welcome(self.):
        self.__hello()
        

p = person()
p.welcome() # accessing the private method through public method
p.__hello() # accessing private method directly isn't allowed.
