# Week 11: --> Task 3
# File: ACT_Python_4p3_secenah.py
# Date:    11/07/2025
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
# This script calculates the percentage of heads or tails for a set number of coin flips.

import random
#get inputs
x = float(input("Number of times to flip a coin: "))
#initialize variables
headCount = 0
tailCount = 0
#set loop conditions
for i in range(0, int(x), 1):
    flip = random.randint(0, 1)
    if flip==0:
        tailCount += 1
    elif flip==1:
        headCount += 1
#calculate flip percentages
percentHeads = round(((headCount/x)*100), 2)
percentTails = round(((tailCount/x)*100), 2)
#print percentages
print(f"Tails percentage: {percentTails}%")
print(f"Heads percentage: {percentHeads}%")

