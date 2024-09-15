#set
''' set is a mutable datatype but can only have immutable data type value as an element,
that means set can't have list, dictionary as an element'''
'''Yes, you can have a tuple as an element in a Python set. 
This is because tuples are immutable, and set elements must be immutable and hashable. 
Since tuples cannot be changed after they are created, they are hashable and can be included in a set.'''

s = {12,312,232,12,341,12}

# Set is a mutable data type like (dictionary and list) and set are unindexed

# Empty set
e = set() #Empty set
print(type(e)) #<class 'set'>

set = {1,1,1,2,34,5,46,6435,4,23,2,24,5,5,5,5,5}
print(set) #{1, 2, 6435, 34, 5, 4, 46, 23, 24} (set doesn't repeat/store same element)

set.add("harrycode")
print(set) #{1, 2, 6435, 34, 5, 4, 'harrycode', 46, 23, 24}

set.remove("harrycode")
print(set) # {1, 2, 6435, 34, 5, 4, 46, 23, 24}

print(len(set)) #9

#clear()

#set.clear() # Clear all the elements of set

# Set union and intersection

s1 = {1,45,6}
s2 = {7,8,1,78}

print(s1.union(s2))  # {1, 6, 7, 8, 45, 78}
print(s1.intersection(s2)) # {1}
