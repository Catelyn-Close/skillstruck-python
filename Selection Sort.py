#challenge
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
inp = int(input("add a number. "))
arr.append(inp)

lister = []
lister.append(min(arr))




def counting(x=1):
    while True:
        nextval = lister[-1] + x
        if nextval in arr:
            lister.append(nextval)
            break
        else:
            x += 1
    if len(lister) == 19:
        return lister
    else:
        counting(x=1)

counting(x=1)

print(lister)
