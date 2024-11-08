#use dictionary to sort names/scores
#sort names by score
#index names and go back to score list
#if any score == the best score
#append to new list and print that
#:) start stuff v
students_and_scores = {}
c = 0
people = [n for n in input("Enter the students names. ").split(" ")]
scores = [n for n in input("Enter the students scores. ").split(" ")]
scores.sort()
lister = []
#functions and working bits________________
#makes correct dictionary 
def counting(c):
    students_and_scores[people[c]] = scores[c]
    c += 1
    if c == len(people):
        return students_and_scores
    else:
       counting(c)
#call func and find max in dictionary
counting(c)
maximum = max(students_and_scores.values())
#checks the list for the highest score
for x, y in students_and_scores.items():
    if y == maximum:
        lister.append(x)
#_______________________________________
#the answer
print(lister)



info= """
casey brownie apple daphney dolly
99 40 78 99 98
"""