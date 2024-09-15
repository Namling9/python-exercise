# Read
'''
f = open("file.txt")
data = f.read()
print(data)
f.close()
'''
# Write()
'''
sts = "This is a python course for data science and machine learning"
f = open("file2.txt", "w")
f.write(sts)

#read()
f = open("file2.txt")
data = f.read()
print(data) #This is a python course for data science and machine learning
f.close()

'''

#readlines()
'''
f = open("file.txt")
data = f.readlines()
print(data, type(data)) #['Hello world, I am namling limbu and data scientist.'] <class 'list'>
f.close()
'''
#readline
'''
f = open("file.txt")

data1 = f.readline()
print(data1) #Hello world, I am namling limbu and data scientist.

data2 = f.readline()
print(data2) # this is python course

data3 = f.readline()
print(data3) # by namling limbu

data4 = f.readline()
print(data4) #Wanna be smart guy???
f.close()
'''
#or
'''
f = open("file.txt")
line = f.readline()

while(line != ""):
    print(line)
    line = f.readline()
    
f.close()
'''


# "a" appending

'''
a = " Thank you"
f = open("file2.txt", "a")

data = f.write(a)

f.close()

'''

# with statement

with open("file.txt") as f : 
    print(f.read())
    
# (you don't have to close file by using with statement.)

