answer = "y"

mylist = []
while answer == "y":
    name = input("input a name ")
    mylist.append(name)
    answer = input("do you want more contacts? y/n" )
    

mylist.sort()
print(mylist)