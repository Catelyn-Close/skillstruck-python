stopper = """
#Checkpoint
my_list1 = [[40, 45, 50], [6, 7, 8], [100, 200, 300], [50, 60, 70], [9, 0, 1]]

rows = 5
cols = 3

for i in range(rows):
    for j in range(cols):
        my_list1[i][j] = my_list1[i][j] + 3 

print(my_list1)

#Checkpoint Multiply List Values

my_list = [[0, 1, 2], [10, 15, 20], [100, 200, 300], [5, 6, 7]]

num = int(input("input a number. "))

cols = 3
rows = 4

for i in range(rows):
    for j in range(cols):
        my_list[i][j] = my_list[i][j] * num
print(my_list)
"""
#Find the Largest Value
x = int(input("What is the first number?"))
y = int(input("What is the second number?"))
z = int(input("What is the third number?"))
my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]


big = max(max(row)for row in my_list)
        
print(big)
