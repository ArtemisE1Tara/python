# PYTHON 3: REPETITION FLOW (CONDITIONAL STRUCTURES) --> Task 4
# File: ACT_Python_3p4secenah.py
# Date:    10/31/2025
# By:      Ahmed Secen
# Section: 018
# Team:    2
# 
# ELECTRONIC SIGNATURE
# Ahmed Secen
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This script determines the winner of a set number of dice games based on how many rounds they won.

import random

#get player name inputs
player1 = input('Player 1 name: ')
player2 = input('Player 2 name: ')
#get number of rounds to be played
x = float(input('Number of rounds to be played: '))

#initialize variables
roundCount = 0
player_1_winCount = 0
player_2_winCount = 0

#set condition
while roundCount<=x:
    #get random player roll values
    player_1_rollValue = random.randint(1,6)
    player_2_rollValue = random.randint(1,6)

    #update player win counts based on who won
    if player_1_rollValue>player_2_rollValue:
        player_1_winCount = player_1_winCount + 1
    else:
        player_2_winCount = player_2_winCount + 1
    roundCount = roundCount + 1

#determine winners
if player_1_winCount>player_2_winCount:
    print(f'{player1} wins!')
elif player_2_winCount>player_1_winCount:
    print(f'{player2} wins!')
#determines tie
elif player_2_winCount>player_1_winCount:
    print(f"It's a tie!")


