code = { "a": "q", "b": "x", "c": "j", "d": "z", "e": "v", "f": "p", "g": "k", "h": "u", "i": "w", "j": "y", "k": "b", "l": "t", "m": "r", "n": "d", "o": "h", "p": "s", "q": "e", "r": "a", "s": "i", "t": "f", "u": "l", "v": "g", "w": "o", "x": "n", "y": "c", "z": "m", " ": "1" }

text = input("input your sentence. ")

char = []
number = len(text)
counter1 = 0
counter2 = 1

while counter1 != number:
    text2 = text[counter1:counter2]
    char.append(text2)
    counter1 += 1
    counter2 += 1
codecode = []
for char in text:
    if char in code:
        codecode.append(code[char])
        
print("".join(codecode))
