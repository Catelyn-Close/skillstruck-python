###  Functions
def numsforcalc(n=0):  # n is selecting the array element
    ''' 
    This function changes the boolean in the rules dictionary 
    according to the user input 

    example:
    user1 input: paper
    user2 input: rock

    rules1dict  = {
    "rock1" : False,
    "paper1" : True,
    "scissors1" : False,
    "rock2" : True,
    "paper2" : False,
    "scissors2" : False
    }
    '''
    ## setting up the dictionary for comparison and scoring
    for key in rules1dict:
        rules1dict[key] = False
    
    if allplayera[n] != allplayerb[n]:
        for x,y in rules1dict.items():
            if x in allplayera[n]:
                rules1dict[x] = True
        for x,y in rules1dict.items():
            if x in allplayerb[n]:
                rules1dict[x] = True
    print(rules1dict) #debug



def calculating(reala, realb,m,l):
    ## read the dictionary
    rock1 = rules1dict.get("rock1", False)
    paper1 = rules1dict.get("paper1", False)
    scissors1 = rules1dict.get("scissors1", False)
    rock2 = rules1dict.get("rock2", False)
    paper2 = rules1dict.get("paper2", False)
    scissors2 = rules1dict.get("scissors2", False)
    values = list(rules1dict.values())

    # calculate the player score for this round
    if values[m] == True and values[l] == True:
        playerascore += 1
        playerbscore += 1
        print(playerascore)
        return playerascore, playerbscore
    elif rules1dict["rock1"] and rules1dict["paper2"] == True:
        playerbscore += 1
    elif rules1dict["rock1"] and rules1dict["scissors2"] == True:
        playerascore += 1 
    elif rules1dict["paper1"] and rules1dict["rock2"] == True:
        playerascore += 1
    elif rules1dict["paper1"] and rules1dict["scissors2"] == True:
        playerbscore += 1
    elif rules1dict["scissors1"] and rules1dict["rock2"] == True:
        playerbscore += 1
    elif rules1dict["scissors1"] and rules1dict["paper2"] == True:
        playerascore += 1
    print("r1 stats: \n", "Player A: " playerascore, "\n", "Player B: ", playerbscore)
    ## update the player's total score
    reala += playerascore
    realb += playerbscore
    
    return 

####  State variables
hi = 2
a = "rock1 paper1 scissors1@scissors2 paper2 rock2"
playerascore = 0
playerbscore = 0
reala=0
realb=0
rules1dict = {
    "rock1" : False,
    "paper1" : False,
    "scissors1" : False,
    "rock2" : False,
    "paper2" : False,
    "scissors2" : False
}




# User input and set up

write = input("input both sides")
moves = write.split('@') #creates a 2 element array, player 1 in element 0
allplayera = moves[0].split() # create a 3 element array for P1 moves
allplayerb = moves[1].split()  # create a 3 element array for P2 moves




# print("NUMS!!!!!!!") #debug
# print("START!!!!!!!!!") #debug
# print(allplayera[1]) #debug
# print(allplayerb[1]) #debug




# Round 1, compare array elements[0]
numsforcalc()
calculating(reala, realb, m, l)



print(reala)
print(realb)
print("r2 stats")
numsforcalc(1)
calculating(playerascore, playerbscore,1, 1)
print(reala)
print(realb)
print("r3 stats")
numsforcalc(n=2)
calculating(playerascore=0, playerbscore=0,m=2, l=2)
print(reala)
print(realb)



#tying is broke currently




these = """
rock1 paper1 scissors1@scissors2 paper2 rock2

paper1 rock1 scissors1@scissors2 paper2 rock2
"""

stuf = """
if not hasattr(calculating, first_run):
        reala=0
        realb=0
        calculating.first_run = 0
        print("ITS WORKING!!!!!!!!!??????????!!!!!!???")


pla = ["one1", "two2", "three3"]

plab = ["one", "two", "three"]
dictpla = {
    "one" : True, 
    "two" : False, 
    "three" : False,
    "one1" : True,
    "two2" : False,
    "three3" : False
}
plas = 0
plabs = 0
m = 0
l =3
values = list(rules1dict.values())
if values[m] == True and values[l] == True:
    plas += 1
    plabs += 1
else:
    print(":(")

print(plas, plabs)

"""