#checkpoint
stopper = """
stack = []

stack.append("a")
stack.append("b")
stack.append("c")
stack.append("d")

stack.pop()

print(stack)
#challenge Stack Scramble
first = "r"
second = "t"
third = "s"
fourth = "y"
fifth = "o"
stack = []

stack.append(third)
stack.append(second)
stack.append(fifth)
stack.append(first)
stack.append(fourth)
print(stack)
"""
#Challenge foods with the letter S
answer = ["apples", "steak", "potatoes", "carrots"]
add = input("The word with S. ")

if "s" in add:
    answer.append(add)
    print(answer)
else:
    print("The input doesn't have the letter s ")

