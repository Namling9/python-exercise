#1. Write a program to find the greatest of four numbers entered by the user.
'''
a = int(input("First number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
d = int(input("Fourth number: "))

if(a>b and a>c and a>d):
    print("The greatest number is a : ", a)

elif(b>a and b>c and b>d):
    print("The greatest number is b : ", b)
    
elif(c>a and c>b and c>d):
    print("The greatest number is c: ", c)

else: print("The greatest number is d: ", d) '''


'''2. Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user.'''
    
'''math = int(input("Enter the marks of Math : "))
science = int(input("Enter the marks of Science : "))
computer = int(input("Enter the marks of Computer: "))


total =100* (math+science+computer)/300


if(total>=40 and math >=33 and science>=33 and computer>=33):
    print("You have passed the exam")

else: print("You have failed the exam") '''

'''3. A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams'''

'''
comment = "A spam comment is defined as a text containing following keywords: Make a lot of money”, “buy now”, “subscribe this”, “click this."



if("Make a lot of money" or "buy now" or "subscribe this " or "click this" in comment):
    print("Spam")

else: print("not spam")  '''

#4. Write a program to find whether a given username contains less than 10 characters or not.
'''
username = input("Enter your username: ")

if(len(username)>10):
    print("Your username contains character more than 100")
    
else: print("Your username contains less character than 100")


'''
# 5. Write a program which finds out whether a given name is present in a list or not.\
'''
names = ["Namling", "NASA","FBI"]

n = input("Enter the name you want to find: ")

if(n in names):
    print("Name is present in the list: ", n)

else: print("Name is not present in the list: ", n) '''


'''6. Write a program to calculate the grade of a student from his marks from the 
following scheme:
90 – 100 => Ex
80 – 90 => A
70 – 80 => B
60 – 70 =>C
50 – 60 => D
<50 => F
'''

'''
marks = int(input("Enter your total percentage: "))

if(marks>= 90 and marks <=100):
    print("Grade: Excelllent")

elif(marks>=80 and marks<90):
    print("Grade: 'A'")

elif(marks>= 70 and marks <80):
    print("Grade: 'B'")
    
elif(marks>=60 and marks <70):
    print("Grade: 'C'")

elif(marks>=50 and marks<60):
    print("Grade : 'D'")

elif(marks >= 0 and marks<50):
    print("Fail")

else: print("invalid") '''

#7. Write a program to find out whether a given post is talking about “Harry” or not

post = "aosdfhuaiowhefioahefioa Harry is good teacher"

if("Harry" in post):
    print("The post is talking about Harry")

else: 
    print("The post is not talking about Harry")