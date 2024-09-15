friends = ["Anjal", "Roshan", "Silu", "robo"]

print(friends)

# append()
friends.append("Tyson")

print(friends)  # ["Anjal", "Roshan", "Silu", "robo", "Tyson"]


# Sort()
numbers = [1,5,42,2,0,12,3,5,4,8,9,6,7,10,14]

print(numbers) #[1, 5, 42, 2, 0, 12, 3, 5, 4, 8, 9, 6, 7, 10, 14]

numbers.sort() 

print(f"Sorted numbers: {numbers}") #Sorted numbers: [0, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10, 12, 14, 42]


# Reverse()
numbers.reverse()
print(f"Reversed numbers: {numbers}") #Reversed numbers: [42, 14, 12, 10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0]


# insert()

numbers.insert(3,30) # Inserting value 30 in index 3 of the numebr list.

print(numbers) #[42, 14, 12, 30, 10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0]

# pop()

print(numbers.pop(3)) #30

print(numbers) #[42, 14, 12, 10, 9, 8, 7, 6, 5, 5, 4, 3, 2, 1, 0]

# Remove()

numbers.remove(5)

print("Remove (5): ",numbers) #Remove (5):  [42, 14, 12, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(len(numbers)) #14

