number = int(input("input a number. "))
pnum = True

ranger = range(2, number)

for i in ranger:
    if number % i == 0:
        pnum = False

    

if pnum:
    print(str(number) + " is a prime number")
else:
    print(str(number) + " is not a prime number")