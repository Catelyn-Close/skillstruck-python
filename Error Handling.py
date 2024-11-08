stop = """
#Checkpoint
variable = "string1"

try:
    print(variable)
except:
    print("you really messed that up?")
else:
    print("not impressed")
finally:
    print("not gonna work")
#Challenges Pizza party
vari1 = int(input("pizza slices "))
vari2 = int(input("people at party "))
try:
    print(vari1 // vari2)
except:
    print("Your code doesn't account for if a user tries to enter 0 people")
else:
    print("There is no problem")
finally:
    print("Your exception handling is complete")
"""
#Challenge sunflower seeds
sunflowers = input("How many sunflowers? ")
try:
    print(sunflowers * 300)
except:
    print("There is a problem")
else:
    print("There is no problem")
finally:
    print("Your exception handling is complete")

