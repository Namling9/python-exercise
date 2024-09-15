# Slicing 

name = "Harry"

nameshort = name[0:3]  # Start from index 0 to all the way till 3 (excluding 3).

print(nameshort) # output : Har

# Negative Slicing

print(name[-4 : -1])  #arry

alphabets = "abcdefghijklmnopqrstuvwxyz"

print(alphabets[0:10:4]) # output : aei

name[:5] # name[0:5]

name[0:] # name[0:5]


# String Function

print("Length: ", len(alphabets)) #26

print(name.endswith("rry")) # True

print(name.startswith("Ha")) #True

print(alphabets.capitalize()) # Abcdefghijklmnopqrstuvwxyz

print(name.lower())

print(name.upper())

print(name.title()) # Abcdefghijklmnopqrstuvwxyz

print(name)

print(name.replace("Harry", "carry"))

print("dadf: ",name)
# Exercise

''' 1. Write a python program to display a user entered name followed by Good 
Afternoon using input () function. '''


name = input("What is your name: ")

print(f"Good afternoon {name}")

'''2. Write a program to fill in a letter template given below with name and date.

letter = 
Dear <|Name|>,
You are selected!
<|Date|>

'''


letter = '''
Dear <|Name|>,
You are selected!
<|Date|> '''

print(letter.replace("<|Name|>", name).replace("<|Date|>", "2024/06/09"))

# 3. Write a program to detect double space in a string.

msg = "Hello everyone good to see you  all"

print(msg.find("  "))

# 4. Replace the double space from problem 3 with single spaces.

print(msg.replace("  ", " "))

''' 5. Write a program to format the following letter using escape sequence 
characters

letter = "Dear Harry, this python course is nice. Thanks!"

'''

letter2 = "Dear Harry, \n \n\t this python course is nice. \n \n Thanks!"

print(letter2)
print(letter2.upper())
print(letter2)


# logic 

a = "dad"

b = a[::-1] # reversing string

print(b)

if(a==b):
    print("dad")

else:
    print("not dad")
    
    
a[::-1] # Reversing string