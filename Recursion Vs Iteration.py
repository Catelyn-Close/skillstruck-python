#checkpoint
stopper = """
x = int(input("input a number. "))

def factorial(x):
    if x <= 1:
        return 1
    else:
        return x * (factorial(x - 1))

print(factorial(x))

#Challenge Add the list
list_of_nums = [int(n) for n in input().split()]
print(list_of_nums)

def sums(list_of_nums):
    if not list_of_nums:
        return 0
    else:
        return list_of_nums[0] + sums(list_of_nums[1:])
        
print(sums(list_of_nums))
"""
#Fibonacci challenge

ranger = int(input("input a number for range. "))
def fib(ranger, c1=0, c2=1, starter = [0, 1]):
    if len(starter) != ranger:
        adder = starter[c1] + starter[c2]
        starter.append(adder)
        return fib(ranger, c1 + 1, c2 + 1, starter)
    elif len(starter) == ranger:
        return starter[:ranger]
    
    
print(fib(ranger))

    