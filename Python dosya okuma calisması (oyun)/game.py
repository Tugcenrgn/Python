# This program reads the movements of the players
# whose number of moves are determined from the file
# and plays the number of rounds entered. 
# at the end, it finds the score at the end of the rounds.

import fileinput
import string

def powerCalculater(letter):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(letter)+1

def scoreCalculater(power1, power2):
    return power1-power2


fPlayer1 = open("player1_moves.txt", "r")
fPlayer2 = open("player2_moves.txt", "r")
fCards = open("cards.txt", "r")
fPlayer1.seek(0)
player1moves = 0
player2moves = 0
cardLetter1 = ""
cardLetter2 = ""
score = 0
i=0
numberOfRounds = int(input("number of rounds: "))

for i in range(numberOfRounds):
    player1moves = int(fPlayer1.readline())
    player2moves = int(fPlayer2.readline())
    fCards.seek(player1moves-1)
    cardLetter1 = fCards.read(1)
    fCards.seek(player2moves-1)
    cardLetter2 = fCards.read(1)
    
    print("\n"+ str(i+1) + ". round \n")
    print("card number of player1:  " + str(player1moves))
    print("card number of player2:  " + str(player2moves))
    print("card letter of player1:  " + cardLetter1)
    print("card letter of player2:  " + cardLetter2)   
    print("power of player1's card: " + str(powerCalculater(cardLetter1)))
    print("power of player2's card: " + str(powerCalculater(cardLetter2)))
    print("old score before the round: " + str(score))

    score = scoreCalculater(powerCalculater(cardLetter1), powerCalculater(cardLetter2))

    print("current score after the round: " + str(score))
    
    if i==numberOfRounds-1:
        print("\n Total score:  " + str(score))


