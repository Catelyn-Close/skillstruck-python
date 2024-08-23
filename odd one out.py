words = input("Input a list of words separated by a space. ").split()
lettercount = {}

for word in words:
    first = word[0].lower()
    if first in lettercount:
        lettercount[first] += 1
    else:
        lettercount[first] = 1

maxkey = max(lettercount, key=lettercount.get)
for word in words:
    if word[0].lower() == maxkey:
        print(word)
        
        
