# HW Week 11: --> Task 2
# File: HW_Python4_Task2_secenah.py
# Date:    11/12/2025
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
# This script simulates dice game where the user predicts if the next value if higher, lower, or a tie compared to the previous value.

#get inputs
import random
from colorama import Fore, Style

#get user input
numRounds = float(input("Enter the amount of rounds to play: "))
#initialize variables
initialRoll = random.randint(1, 6)
rollValue = 0
result = ''
winCount = 0
loseCount = 0

#input checks
if numRounds<0:
    print("Invalid input. Must be a positive integer.")
    exit()
elif not numRounds.is_integer():
    print("Invalid input. Must be a positive integer.")
    exit()
else:
    #setup for loop
    for i in range(0, int(numRounds), 1):
        print(f"Initial roll value: {initialRoll}\nWill the next roll be\n1. Higher?\n2. A tie?\n3. Lower?")

        selection = float(input("Prediction: "))
        rollValue = random.randint(1, 6)

        #determine correctness of prediction
        if rollValue>initialRoll and selection==1:
            result = Style.BRIGHT + Fore.GREEN + 'Correct' + Style.RESET_ALL
            winCount = winCount + 1

        elif rollValue>initialRoll and selection!=1:
            result = Style.BRIGHT + Fore.RED + 'Incorrect' + Style.RESET_ALL
            loseCount = loseCount + 1

        elif rollValue==initialRoll and selection==2:
            result = Style.BRIGHT + Fore.GREEN + 'Correct' + Style.RESET_ALL
            winCount = winCount + 1

        elif rollValue==initialRoll and selection!=2:
            result = Style.BRIGHT + Fore.RED + 'Incorrect' + Style.RESET_ALL
            loseCount = loseCount + 1

        elif rollValue<initialRoll and selection==3:
            result = Style.BRIGHT + Fore.GREEN + 'Correct' + Style.RESET_ALL
            winCount = winCount + 1

        elif rollValue<initialRoll and selection!=3:
            result = Style.BRIGHT + Fore.RED + 'Incorrect' + Style.RESET_ALL
            loseCount = loseCount + 1

        initialRoll = rollValue
        print(result)

    #calulate win percentage
    percentWins = (winCount/numRounds)*100

    #output results
    print(f"Number of rounds: {numRounds}\nPercent wins: {percentWins}%")

