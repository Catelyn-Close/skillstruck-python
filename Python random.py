#import random cause its built into python
#random.random for decimals below 0
#randint for ints
import random
x = random.randint(0,10)

print(x)
#random sample allows choose how many
lister = random.sample(range(0,10),5)
print(lister)
#checkpoint
import random
x = random.random()
print(x)

c = random.randint(0,5)
print(c)

v = random.sample(range(0,100), 3)
print(v)
#two dice roll challenge
a = random.randint(1,6)
b = random.randint(1,6)

total = a + b
print(total)
#challenge random percentage
d = random.random()
f = round(d, 2)
print(f)