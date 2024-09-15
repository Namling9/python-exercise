# set and dictionary

''' 1. Write a program to create a dictionary of Hindi words with values as their English
translation. Provide user with an option to look it up!
'''

'''dictionary = {
    "namaste": "Greetings",
    "dhanyavad": "thank you",
    "kya hai": "what is",
    "suwagatam": "welcome",
    "madat": "help"
}

word = input("Enter the word you want meaning of: ")

print(dictionary[word]) '''

'''2. Write a program to input eight numbers from the user and display all the unique 
numbers (once).'''

'''s = set() # empty set
for i in range(8):
    num = int(input("Enter a number: "))
    s.add(num)

print(s) '''

'''3. Can we have a set with 18 (int) and '18' (str) as a value in it?'''
#yes
'''s = {18, "18"}
print(s) # {18, '18'} '''

'''4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''

'''
s = set()
s.add(20)
s.add(20.0)
s.add('20')

print(len(s)) #2
'''

'''5. s = {}
What is the type of 's'? 

print(type(s)) # class <'dict'>

'''

'''6. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique.'''


d = {}

for i in range(4):
    name = input("Enter your name: ")
    lang = input("Enter your fav language: ")
    d.update({name:lang})

print(d)  

'''7. If the names of 2 friends are same; what will happen to the program in problem 
6?

If friends are same second value will overwrite the frist value of same name in dictionary 
which result only three output in dictionary if 2 names are same out of 4.
{'namling': 'python', 'robo': 'php', 'tyson': 'java'}
'''

'''8. If languages of two friends are same; what will happen to the program in problem 
6?

-> It will print all values of dictionary with all 4 values same or  not.
{'namling': 'python', 'tyson': 'python', 'robo': 'python', 'nam': 'java'}'''


'''9. Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]

-> NO, 1st we can't have list inside set as an element and second, Indexing is not allowed in set'''


