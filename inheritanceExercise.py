#1. Create a class (2-D vector) and use it to create another class representing a 3-D vector.

# class vector2D:
    
#     def __init__(self,x,y):
        
#         self.x = x 
#         self.y = y

# class vector3D(vector2D):
    
#     def __init__(self,x,y,z):
        
#         super().__init__(x,y)
#         self.z = z
    
#     def show(self):
#         print(f"{self.x} {self.y} {self.z}")
     

# v3 = vector3D(1,2,3)
# v3.show()
        
'''2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
‘Pets’. Add a method ‘bark’ to class ‘Dog’.
'''

# class animals:
    
#     pass

# class pets(animals):
    
#     pass

# class dog(pets):
    
#     def bark(self):
        
#         print("Bow Bow")
        
# dog1 = dog()
# dog1.bark()


#3. Create a class ‘Employee’ and add salary and increment properties to it
#Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
#which changes the value of increment based on the salary.

# class Employee:
   
#     def __init__(self, name, age, jobtitle):
        
#         self.name = name
#         self.age = age
#         self.jobtitle = jobtitle
    
#     @property
#     def salary(self):
#         return self.s
    
#     @salary.setter
#     def salary(self,value):
#         incr = value * 0.10
#         self.s = value + incr
        

# e = Employee("john", 30, "AI Engineer")

# e.salary = 100000
# print(e.salary) # 110000

'''4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
operators ‘+’ and ‘*’ which adds and multiplies them.'''

# class complex:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag
    
#     def __add__(self, other):
#         return complex(self.real + other.real, self.imag + other.imag)
    
#     def __mul__(self, other):
#         real_part = self.real * other.real - self.imag * other.imag 
#         imag_part = self.real * other.imag + self.imag * other.real
#         return complex(real_part, imag_part)
    
#     def __str__(self):
        
#         return f"{self.real} + {self.imag}"


# c1 = complex(1,-3)
# c2 = complex(2,4)

# print(f"{c1+c2}i")
# print(c1*c2)

# s = ['python', 'hub']

# print(s[:1][-1])

#5. Write a class vector representing a vector of n dimensions. Overload the + and * 
#operator which calculates the sum and the dot(.) product of them.

class vector:
    
    def __init__(self,x,y,z):
        
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        result = self.x + other.x, self.y + other.y, self.z + other.z
        return result
    
    def __mul__(self, other):
        result = self.x * other.x + self.y*other.y + self.z*other.z
        return result
    
    def __str__(self):
        return f"vector{self.x} {self.y} {self.z}"
    
v1 = vector(1,2,3)
v2 = vector(4,5,6)
v3 = vector(7,8,9)

print(v1+v2)
print(v1*v2)

        
