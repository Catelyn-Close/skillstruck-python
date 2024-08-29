#checkpoint

rows = 3
columns = 5
pets = "string1" "string2" "string3" "string4" "string5"

loop = [[j for j in pets] for i in range(rows)]
print(loop)

#challenge multiply by the number of rows
rows = int(input("how many rows? "))
mylist = [1, 2, 3, 4, 5]
real = [i * rows for i in mylist]
loop = [[j for j in real] for i in range(rows)]
print(loop)


#challenge weather watcher
rows = input("Input a list of weather").split()
length = len(rows)
a, b, c = rows

d, e, f = cols

stuff = [[a + d, a + e, a + f], [b + d, b + e, b + f], [c + d, c + e, c + f]]
cols = ["windy", "breezy", "calm"]

loop = [[j for j in stuff] for i in range(length)]
#  sun rain snow

