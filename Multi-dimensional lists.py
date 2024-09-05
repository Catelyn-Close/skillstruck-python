stopper = """
#checkpoint 
rows = 5
cols = 3
list = []

for i in range(rows):
    ist = []
    for j in range(cols):
        list.append(5)

print(list)
#Secret Agent Name Generator

Firstn = ["Sam", "Max", "Bandit", "Rover"]
Lastn = ["Brown", "Wyre", "MaxiMillian", "Fender"]
listist = []
for i in Firstn:
    empty = []
    for j in Lastn:
        empty.append(i + j)
print(empty)
"""
#Fruit Blender
lista = ["apple", "grape", "peach", "cinnamon", "vanilla"]
#listb = ["kumquat", "starfruit", "papaya"]
listb = input("Input a list of fruits. ").split()
lister = []
for i in listb:
    list1 = []
    for j in lista:
        list1.append(i + " " + j)
    lister.append(list1)
print(lister)
#kumquat starfruit papaya