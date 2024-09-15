'''
Input data: Create a dictionary of students where the key is the student's
name and the value is a dictionary containing subjects and their respective scores. Example:

students = {
    'Alice': {'Math': 78, 'Science': 82, 'English': 90},
    'Bob': {'Math': 65, 'Science': 70, 'English': 60},
    'Charlie': {'Math': 85, 'Science': 80, 'English': 75},
    'Diana': {'Math': 95, 'Science': 92, 'English': 98},
    'Eve': {'Math': 45, 'Science': 50, 'English': 40}
}

Calculate average scores for each student using list comprehension. Store the averages in a dictionary where keys are student names and values are their averages.

Assign grades based on the average score:

A: 90-100
B: 80-89
C: 70-79
D: 50-69
F: Below 50

Store the grades in another dictionary.

Report students who passed (average score ≥ 50) and students who failed (average score < 50) using dictionary comprehension.

Find the top 3 students based on average scores using list comprehension.

Create a set of students who scored the highest in each subject using set comprehension.

Bonus:
Handle ties for the highest score in any subject.
Use Python functions to modularize your code (e.g., one function for calculating averages, another for assigning grades, etc.).
'''

# list2 = [input(f"Enter the element: ") for i in range(5)]

# print(list2)

#students = {}

# num_students = int(input("Enter the number of students: "))

# for i in range(num_students):
#     name = input(f"\nEnter name for student {i+1}: ")

#     math = int(input(f"Enter {name}'s Math score: "))
#     science = int(input(f"Enter {name}'s Science score: "))
#     english = int(input(f"Enter {name}'s English score: "))

#     # Add to the students dictionary
#     students[name] = {'Math': math, 'Science': science, 'English': english}

# print("\nFinal Students Dictionary:")
# print(students)

students = {input("Enter the name of student: "): {'Math': int(input("Enter the math score: ")), 
                                                  'Science': int(input("Enter the science score : ")),
                                                  'English': int(input("Enter the english score: "))} 
           for i in range(1)}

print(students)

average = [sum(score.values())/ len(score) for score in students.values()]
print(average)

if average >= 90 and average <= 100:
    print("A")
elif average >= 80 and average < 90:
    print("B")
elif average >= 70 and average < 80:
    print("C")
elif average >= 50 and average < 70:
    print("D")
elif average < 50:
    print("F")
else: print("Not valid input")

result = { 
          "Passed" : {student : marks for student,marks in average.items() if marks >=50},
          "Failed": {student : marks for student,marks in average.items() if marks <50}}
print(result)

