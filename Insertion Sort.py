#challenge
arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
inp = int(input("Add a number: "))
arr.append(inp)

lister = []
lister.append(arr[0])

def counter():
    for i in arr:
        inserted = False
        for j in range(len(lister)):
            if i <= lister[j]:
                lister.insert(j, i)
                inserted = True
                break
        if not inserted:
            lister.append(i)
counter()

print(lister)


