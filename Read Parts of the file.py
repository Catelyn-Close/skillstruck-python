#checkpoint
codestopper = """
files = open("speech.txt", "r")

print(files.readline())
print(files.readline())
print(files.read(10))

files.close()

#challenge, read a specific number of characters

user = int(input("pick a number"))

file = open("speech.txt", "r")

print(file.read(user))

file.close()
"""

vari = open("speech.txt", "r")
words = vari.read()
swords = words.split()
gth = len(swords)
print(gth)
vari.close()