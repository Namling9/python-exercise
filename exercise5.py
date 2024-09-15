# loops

# 1. Write a program to print multiplication table of a given number using for loop.

#n = int(input("Enter the number you want multiplication of: "))

# While loop
# i = 0
# while i <= 10:
#     print(f"{n} * {i} = {n*i}")
#     i+=1

# for loop

# for i in range(10+1):
#     print(f"{n} * {i} = {n*i}")
    

'''2. Write a program to greet all the person names stored in a list ‘l’ and which starts 
with S.
l = ["Harry", "Soham", "Sachin", "Rahul"] '''

# l = ["Harry", "Soham", "Sachin", "Rahul"] 

# for i in l : 
    
#     if(i.startswith("S")):
#         print(f"Hello {i}")

# i = 0
# while(i<len(l)):
    
#     if(l[i].startswith("S")):
#         print(f"Hello {l[i]}")
#     i+=1
    

#4. Write a program to find whether a given number is prime or not.

# n = int(input("Enter a number to find prime or not: "))

# for i in range(2,n):
   
#     if(n%i == 0):
#         print(f"{n} is not a prime number")
    
#     break

# else: print(f"{n} is a prime number")
    
#print(f"{n%2==0}")

#5. Write a program to find the sum of first n natural numbers using while loop.

# n = int(input("Enter a number to find sum of natural numbers: "))
# sum = 0
# for i in range(n+1):
#     sum += i

# print(sum)
# sum = 0
# i = 0
# while (i<n+1):
#     print(i)
#     sum+=i
#     i+=1
# print(sum)

# 6. Write a program to calculate the factorial of a given number using for loop.

'''n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1,n+1):
     
    fact *= i
 
print(fact) '''

'''7. Write a program to print the following star pattern.
  *
 ***
***** for n = 3 '''
'''
n = int(input("Enter a number: "))

for i in range(n+1):
    
    print(" "*(n-i),end="" )
    print("*" * (2*i-1), end="")
    print("") '''
  
'''8. Write a program to print the following star pattern:
*
**
*** for n = 3 '''

'''
n = int(input("Enter a number: "))

for i in range(n+1):
    print("*"*i, end="")
    print(" "*(n-i), end="")
    print("") '''
    
'''9. Write a program to print the following star pattern.
* * *
*   * for n = 3
* * * 
'''
'''
n = int(input("Enter a number: "))

for i in range(1,n+1):
    
    if(i ==1 or i == n):
        print("*" *n, end="")
    
    else: 
        print("*", end="")
        print(" "*(n-2), end="")
        print("*",end="" )
    
    print() '''

#10. Write a program to print multiplication table of n using for loops in reversed order
'''
n = int(input("Enter a number: "))

for i in range(10):
    print(f"{n} x {10-i} = {n*(10-i)}") '''