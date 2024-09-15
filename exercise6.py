# 1. Write a program using functions to find greatest of three numbers.

'''def find(a,b,c):
    
    if a>b and a>c:
        print(f"{a} is the greatest number")
        
    elif b>a and b>c:
        print(f"{b} is the greatest number")
        
    else:print(f"{c} is the greatest number")

a = int(input("Enter the number: "))
b = int(input("Enter the number:"))
c = int(input("Enter the number: "))

find(a,b,c) '''

#2. Write a python program using function to convert Celsius to Fahrenheit.

'''def convertF(celsius):
    
    print(f"Fahrenheit is : {(celsius*9/5)+32}")
    
celsius = int(input("Enter the number: "))
convertF(celsius) '''

#3. How do you prevent a python print() function to print a new line at the end
'''
print("hello", end =" ")
print("world")  # output : hello world '''

#4. Write a recursive function to calculate the sum of first n natural numbers.

'''def sum(n):
    if n == 1 or n == 0:
        return n
    
    return n + sum(n-1)

n = int(input("enter the number: "))
print("The sum of first n natural numbers : ",sum(n)) '''


'''5. Write a python function to print first n lines of the following pattern:
***
** - for n = 3
*'''
'''
def pattern(n):
    
    for i in range(n):
        print("*"*(n-i), end="")
        print(" "*i, end="")
        print("")

n = int(input("enter the number: "))
pattern(n) '''

# 6. Write a python function which converts inches to cms.

'''
def convertCM(n):
    
    return 2.54 * n

n = int(input("enter the number: "))
print(f"{n} inches is {convertCM(n)}cm") '''


'''7. Write a python function to remove a given word from a list ad strip it at the same 
time.
'''

def remove(l):
    



