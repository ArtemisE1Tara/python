# PYTHON 3: REPETITION FLOW (CONDITIONAL STRUCTURES) --> Task 5
# File: ACT_Python_3p5secenah.py
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
# This script determines the winner of multiple rounds of dice based on who 
# reaches or exceeds a target score first.

import random
#get score input
targetValue = float(input('Enter target score: '))

#get player name inputs
player1 = input('Player 1 name: ')
player2 = input('Player 2 name: ')

#initialize variables
player1_rollValue = 0
player2_rollValue = 0
player1_total = 0
player2_total = 0

#set conditions
while player1_total<targetValue and player2_total<targetValue:
    #get random roll values
    player1_rollValue = random.randint(1,6)
    player2_rollValue = random.randint(1,6)

    #update player score totals
    player1_total = player1_rollValue + player1_total
    player2_total = player2_rollValue + player2_total

#determine winners
if player1_total>player2_total:
    print(f"{player1} wins!\n{player1}'s score: {player1_total}\n{player2}'s score: {player2_total}")
elif player2_total>player1_total:
    print(f"{player2} wins!\n{player2}'s score: {player2_total}\n{player1}'s score: {player1_total}")
#determines tie
elif player2_total==player1_total:
    print("It's a tie!\n{player1}'s score: {player1_total}\n{player2}'s score: {player2_total}")

