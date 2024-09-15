#1. Write a program to store seven fruits in a list entered by the user. 

''' Fruits = []

f1 = input("Enter the fruit name: ")
Fruits.append(f1)

f2 = input("Enter the fruit name: ")
Fruits.append(f2)

f3 = input("Enter the fruit name: ")
Fruits.append(f3)

f4 = input("Enter the fruit name: ")
Fruits.append(f4)

f5 = input("Enter the fruits name: ")
Fruits.append(f5)

f6 = input("Enter the fruits name: ")
Fruits.append(f6)

f7 = input("Enter the fruits name: ")
Fruits.append(f7)

Print(f"Seven fruits name: {Fruits}") '''


#2. Write a program to accept marks of 6 students and display them in a sorted manner.

'''Marks = []

s1 = float(input("Enter the marks: "))
Marks.append(s1)

s2 = float(input("Enter the marks: "))
Marks.append(s2)

s3 = float("Enter the marks: ")
Marks.append(s3)

s4 = float(input("Enter the marks: "))
Marks.append(s4)

s5 = float("Enter the marks: ")
Marks.append(s5)

s6 = float("Enter the marks: ")
Marks.append(s6)

Marks.sort()
print(f"Six students marks: ") '''

#3. Check that a tuple type cannot be changed in python

'''a = (12,32,42,12)

a[3] = "harry"
print(a) # error '''

#4. Write a program to sum a list with 4 numbers.

list = [12,23,42,42]

print(sum(list))

# 5. Write a program to count the number of zeros in the following tuple: a = (7, 0, 8, 0, 0, 9)

a = (7, 0, 8, 0, 0, 9)

print(a.count(0)) #3
