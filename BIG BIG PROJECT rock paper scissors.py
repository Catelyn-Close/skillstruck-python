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
    #print(rules1dict) #debug



def calculating(m):
    ## read the dictionary
    rock1 = rules1dict.get("rock1", False)
    paper1 = rules1dict.get("paper1", False)
    scissors1 = rules1dict.get("scissors1", False)
    rock2 = rules1dict.get("rock2", False)
    paper2 = rules1dict.get("paper2", False)
    scissors2 = rules1dict.get("scissors2", False)
    values = list(rules1dict.values())
    this_score_a = 0
    this_score_b = 0
    # calculate the player score for this round
    if values[m] == True and values[m+3] == True:
        this_score_a += 1
        this_score_b += 1
        
    elif rules1dict["rock1"] and rules1dict["paper2"] == True:
        this_score_b += 1
    elif rules1dict["rock1"] and rules1dict["scissors2"] == True:
        this_score_a += 1
    elif rules1dict["paper1"] and rules1dict["rock2"] == True:
        this_score_a += 1
    elif rules1dict["paper1"] and rules1dict["scissors2"] == True:
        this_score_b += 1
    elif rules1dict["scissors1"] and rules1dict["rock2"] == True:
        this_score_b += 1
    elif rules1dict["scissors1"] and rules1dict["paper2"] == True:
        this_score_a += 1
    ## send back this round's score
    return (this_score_a, this_score_b)

####  State variables
hi = 2
a = "rock1 paper1 scissors1@scissors2 paper2 rock2"
this_score_a = 0
this_score_b = 0
total_score_a = 0
total_score_b = 0
rules1dict = {
    "rock1" : False,
    "paper1" : False,
    "scissors1" : False,
    "rock2" : False,
    "paper2" : False,
    "scissors2" : False
}




# User input and set up

write = input("input both sides: ")
moves = write.split('@') #creates a 2 element array, player 1 in element 0
allplayera = moves[0].split() # create a 3 element array for P1 moves
allplayerb = moves[1].split()  # create a 3 element array for P2 moves


# Round 1, compare array elements[0]
m, l, n  = 0, 0, 0
numsforcalc(n)
this_round_score = calculating(m)

#print("r1 stats")
total_score_a += this_round_score[0]
total_score_b += this_round_score[1]
#print("Total Player 1; ", total_score_a)
#print("Total Player 2; ",total_score_b)
#print("--------")


# Round 1, compare array elements[0]
m, l, n  = 1, 1, 1
numsforcalc(n)
this_round_score = calculating(m)
total_score_a += this_round_score[0]
total_score_b += this_round_score[1]
#print("r2 stats")
#print("Total Player 1; ", total_score_a)
#print("Total Player 2; ",total_score_b)
#print("--------")



# Round 1, compare array elements[0]
m, l, n  = 2, 2, 2
numsforcalc(n)
this_round_score = calculating(m)
total_score_a += this_round_score[0]
total_score_b += this_round_score[1]
#print("r3 stats")
#print("Total Player 1; ", total_score_a)
#print("Total Player 2; ",total_score_b)
#print("--------")



#tying is fixed :)




these = """
variation 1
rock1 paper1 scissors1@scissors2 paper2 rock2
variation 2
paper1 rock1 scissors1@scissors2 paper2 rock2
"""


if total_score_a > total_score_b:
    print(total_score_a, total_score_b, "Player 1 Wins!")
elif total_score_a < total_score_b:
    print(total_score_a, total_score_b, "Player 2 Wins!")
else:
    print(total_score_a, total_score_b, "Tie!")

