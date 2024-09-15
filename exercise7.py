# File handling

#1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.
'''
a = "baba black sheep, do you have any wools? Yes sir Yes sir three bags full. twinkle twinkle litle star, How i wonder what you are?"

f = open("poems.txt", "w")
data = f.write(a)

f = open("poems.txt")
text = f.read()
print(text)
f.close()

with open("poems.txt") as f:
    
    data = f.readlines()
    for i in data:
        if "twinkle" in i :
            print("The word 'twinkle' is found in the file.") '''
'''          
f = open("poems.txt")
content = f.read()

if 'twinkle' in content :
    print("The word 'twinkle' is found in the file.")
    
else: print("The word 'twinkle' is not found in the file")

f.close()
'''

'''2. The game() function in a program lets a user play a game and returns the score 
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.
'''
'''
import random

def game(): 
   
   print("You are playing game..")
   score = random.randint(1,100)
   
   #Fetch the hiscore 
   with open("hiscore.txt") as f:
       hiscore = f.read()
       if hiscore != "":
           hiscore = int(hiscore)
       else: 
           hiscore = 0
           
           
   print(f"Your score : {score}")
   
   if(score>hiscore or hiscore ==""):
       
       print(f"Congratulations you got high score : {score}")
       # Write this hiscore in the file
       
       with open("hiscore.txt", "w") as f:
           
           f.write(str(score))
    
   return score

game()
'''

'''3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
different files. Place these files in a folder for a 13 – year old.'''

'''
def multiplication(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} x {i} = {n*i} \n"
    
    with open(f"tables/table_{n}.txt","w") as f:
        f.write(table)
    

for i in range(2,21):
    
    multiplication(i)
        '''

'''4. A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.'''

with open("file2.txt") as f:
    data = f.read()
    print(data)

new_data = data.replace("donkey", "######")

with open("file2.txt", "w") as f:
    f.write(new_data)
    

       