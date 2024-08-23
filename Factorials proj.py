number = int(input("put a number. "))

ranger = range(1, number + 1)

for i in ranger:
    factorial = 1
    for j in range(1, i + 1):
        factorial *=j
   


        

print(factorial)