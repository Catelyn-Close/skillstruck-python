#challenge

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

arr = [10, 32, 4, 90, 15, 20, 89, 1, 3, 45, 42, 87, 91, 18, 25, 76, 38, 12]
inp = int(input("add a number. "))
arr.append(inp)

n = len(arr)
for num in range(n - 1):
    for i in range (n - 1 - num):
        if arr[i] > arr[i+1]:
            swap(arr, i, i + 1)
   
print(arr)

