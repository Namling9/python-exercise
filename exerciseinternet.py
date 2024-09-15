''' 1) Create a program that asks the user to enter their name and their age. Print out a message addressed
to them that tells them the year that they will turn 100 years old. Note: for this exercise,
the expectation is that you explicitly write out the year (and therefore be out of date the next year)'''

# name = input("Enter your name: ")
# age = int(input("Enter you age: "))

# print(f" Hi {name}, You will turn 100 years old in {(2024 - age)+100} A.D")


'''2) Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?'''

# number = int(input("Enter the number: "))

# if number%2 == 0:
#     print(f"{number} is even number.")

# else: print(f"{number} is odd number")

'''3) Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for i in a:
    if i < 5:
        b.append(i)
        
print("List a: ", a) #List a:  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print("List b: ", b) #List b:  [1, 1, 2, 3]

''' 4) Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, 
it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)'''

number = int(input("Enter the number: "))
divisor = []
n =100
for i in range(n):
    if i % number == 0:
        divisor.append(i)
    else: continue

print(divisor) #[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]