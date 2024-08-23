words = {
    1: "razzle", 
    2: "dazzle", 
    3: "scampr", 
    4: "orange", 
    5: "stumpy", 
    6: "garage",
    7: "action",
    8: "attack",
    9: "spacer",
    10: "oddity"
}

lose = False

numguesser = int(input("pick a number 1-10. "))

tword = (words[numguesser])


while lose == False:
    letter = input("guess the first letter of the word. ")
    if letter == tword[:1]:
        print(letter)
        break
    else: 
        print("-")
        break
while lose == False:
    letter = input("guess the second letter of the word. ")
    if letter == tword[1:2]:
        print(letter)
        break
    else: 
        print("-")
        break
while lose == False:
    letter = input("guess the third letter of the word. ")
    if letter == tword[2:3]:
        print(letter)
        break
    else: 
        print("-")
        break
while lose == False:
    letter = input("guess the fourth letter of the word. ")
    if letter == tword[3:4]:
        print(letter)
        break
    else: 
        print("-")
        break
while lose == False:
    letter = input("guess the fifth letter of the word. ")
    if letter == tword[4:5]:
        print(letter)
        break
    else: 
        print("-")
        break
while lose == False:
    letter = input("guess the sixth letter of the word. ")
    if letter == tword[5:6]:
        print(letter)
        break
    else: 
        print("-")
        break


final = input("youve used all your guesses! guess the word or lose now. ")


if final == tword:
    lose = False
    print("You Won! The word was " + str(tword))
else:
    Lose = True
    print("You Lost! The word was " + str(tword))



