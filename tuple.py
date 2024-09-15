''' Tuple are immutable data type like string '''

#tuple 
a = (1,2,3,5,4,6,5,3,4,5,5,6,1,2)

# Empty tuple
b = ()

print(type(a)) # <class 'tuple'>

# tuple with 1 element
c = (1,) # c = (1) will be an integer, comma is necessary while making tuple with one element.

# count()

#count = a.count(5)
print(a.count(5)) # output: 4 because there are four 5 in the tuple

# index
print(a.index(5)) # output: 3 because the first 5 in the tuple is in index 3.



print(len(a)) #14