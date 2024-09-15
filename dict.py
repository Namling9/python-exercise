''' Dictionary is a collection of key-pairs value'''

Marks = {
    "Namling" : 100,
    "Nischal" : 99,
    "Swastika": 99,
    "Arun": 99,
    "Pashupati": 99
}

print(Marks["Namling"]) #100

# items()
print(Marks.items()) #ict_items([('Namling', 100), ('Nischal', 99), ('Swastika', 99), ('Arun', 99), ('Pashupati', 99)])

# keys()
print(Marks.keys()) #dict_keys(['Namling', 'Nischal', 'Swastika', 'Arun', 'Pashupati'])

# Values()
print(Marks.values()) #dict_values([100, 99, 99, 99, 99])

# Update()
Marks.update({"Pashupati": 95})
print(Marks) #{'Namling': 100, 'Nischal': 99, 'Swastika': 99, 'Arun': 99, 'Pashupati': 95}

print(Marks.get("Namling")) #100
print(Marks["Namling"]) #100

#print(Marks.get("Namling1234")) #none
#print(Marks["Namling1234"]) # error

print(Marks.pop("Pashupati")) #95
print(Marks) #{'Namling': 100, 'Nischal': 99, 'Swastika': 99, 'Arun': 99}

print(Marks.popitem()) #('Arun', 99)
print(Marks) #{'Namling': 100, 'Nischal': 99, 'Swastika': 99}

# Empty dictionary
d = {} # Empty dictionary

print(len(Marks)) #3