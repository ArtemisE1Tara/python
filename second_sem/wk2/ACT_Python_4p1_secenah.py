# Activity Python 4: Task 1
# File: ACT_Python_4p1A_secenah.py
# Date:    01/22/2026
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
# This script rolls two dice, adds them together, stores them in a list, and then counts how many times the dies added up to 7.

import random

N = int(input("Number of rolls per two dice: "))

if N<0:
    int(input(("Invalid input. Number must be positive.\nEnter the number of rolls per two dice: ")))
else:
    List = []
    sevenCount = 0
    for i in range(N):
        D1 = random.randint(1,6)
        D2 = random.randint(1,6)

        sum = D1+D2
        List.append(sum)
    
    for n in range(len(List)):
        if List[n]==7:
            sevenCount = sevenCount + 1
    
    print(f"Dice roll sums: {List}\nNumber of times sum is 7: {sevenCount}")