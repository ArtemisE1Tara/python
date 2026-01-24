# Activity Python 1: Task 3
# File: ACT_Python_Task1_secenah.py
# Date:    01/15/2026
# By:      Ahmed Secen
# Section: 008
# 
# Ahmed Secen
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This script guesses a four digit code and outputs the number of correctly guessed digits.

import math
import random

# get inputs
D1 = float(input("First digit: "))
D2 = float(input("Second digit: "))
D3 = float(input("Third digit: "))
D4 = float(input("Fourth digit: "))

# initialize variables
count = 0
guess = 0
D1_correct = 0
D2_correct = 0
D3_correct = 0
D4_correct = 0

none_ct = 0
one_ct = 0
two_ct = 0
three_ct = 0
four_ct = 0

# set up loop condition
while count<1000:
    # setup conditionals
    if D1 == random.randint(0,9):
        D1_correct = 1
    else:
        D1_correct = 0
    if D2 == random.randint(0,9):
        D2_correct = 1
    else:
        D2_correct = 0
    if D3 == random.randint(0,9):
        D3_correct = 1
    else:
        D3_correct = 0
    if D4 == random.randint(0,9):
        D4_correct = 1
    else:
        D4_correct = 0

    # update how many digits were guessed correctly
    if D1_correct+D2_correct+D3_correct+D4_correct==0:
        none_ct = none_ct + 1
    elif D1_correct+D2_correct+D3_correct+D4_correct==1:
        one_ct = one_ct + 1
    elif D1_correct+D2_correct+D3_correct+D4_correct==2:
        two_ct = two_ct + 1
    elif D1_correct+D2_correct+D3_correct+D4_correct==3:
        three_ct = three_ct + 1
    elif D1_correct+D2_correct+D3_correct+D4_correct==4:
        four_ct = four_ct + 1
    
    # update counter
    count = count + 1

print(f"No digits correct: {none_ct}\nOne digit correct: {one_ct}\nTwo digits correct: {two_ct}\nThree digits correct: {three_ct}\nFour digits correct: {four_ct}\nIterations: {count}")



    

    

    
    