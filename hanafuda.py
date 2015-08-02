# keeps the score for the Japanese card game hanafuda 
# ____________________________________________________________

print "This is your hanafuda score calculator. Please answer these questions."

# initial values 
month = 0
a = [(0,0,0)]
sumOne = 0


def data():
    scoresMatch = 0
    while scoresMatch == 0:
        playerOne = int(input("What was player 1's score?: "))
        playerTwo = int(input("What was player 2's score?: "))
        playerThree = int(input("What was player 3's score?: "))
        if playerOne + playerTwo + playerThree == 0: 
            scoresMatch = 1
            return (playerOne, playerTwo, playerThree)
        else:
            print("The scores do not match!")

while month < 12:
    print "-------------------"
    print("The month is:", month+1)
    a.insert(month, data())
    month = month + 1
    sum_playerOne = sum(a[i][0] for i in range (0,month+1))
    sum_playerTwo = sum(a[i][1] for i in range (0,month+1))
    sum_playerThree = sum(a[i][2] for i in range (0,month+1))
    print "The score is player 1:" , sum_playerOne, "player 2:" , sum_playerTwo, "player: 3" , sum_playerThree 
