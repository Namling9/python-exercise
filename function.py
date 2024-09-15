'''email = "namling@gmail.com"
print(email.split("@")) #['namling', 'gmail.com'] '''

# Function defination
'''def hello():
    print("Hello world")
    
# function call
hello() '''

# Function defination
'''def avg():
    
    a = int(input("Enter number: "))
    b = int(input("Enter number: "))
    c = int(input("Enter number: "))
    
    print("Average: ",(a+b+c)/3)

#Function call
avg() '''


'''def greet():
    name = input("Enter your name: ")
    print(f" Hello {name}")

greet()'''

# Function with arguement
# def greet(name):
#     print("Hello", name)
    
# greet("Namling") #Hello Namling
# greet("Genius") # Hello Genius


# Default parameter value function
# def greet(name, ending = "Good morning"):
    
#     print(f"Hello {name}, {ending}")
    
# greet("Namling") # Hello Namling, Good morning
# greet("L", "Good afternoon") #Hello L, Good afternoon


# Recursion

# Recursion is a function which call itself

def factorial(n):
    
    if( n == 1 or n == 0):
        return 1
    
    return n * factorial(n-1)

a = int(input("Enter the number: "))

print(f"The factorial of {a} is : {factorial(a)}")