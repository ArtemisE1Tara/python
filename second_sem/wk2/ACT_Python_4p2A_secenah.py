# Activity Python 4: Task 2
# File: ACT_Python_4p2A_secenah.py
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
# This script computes the Fibonacci sequence.

import math

N = int(input("Enter amount of Fibonacci terms: "))

if N<=0:
    int(input("Invalid input. Must be a positive non-zero integer.\nEnter amount of Fibonacci terms: "))
else:
    List = [0,1]
    for i in range(N-2):
        F = ((List[i-1])+(List[i-2]))
        List.append(F)
    print(f"{List}")