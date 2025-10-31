# PYTHON 3: REPETITION FLOW (CONDITIONAL STRUCTURES) --> Task 2
# File: ACT_Python_3p2_secenah.py
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
# This script calculates the factorial of a number.

import math

x = float(input("Enter a number to find the factorial of: "))

class Solution:
    def Factorial(self):
        i = 0
        factorial = 0
        if x<0:
            return('Invalid input: must be a positive value')
        elif x==0:
            return('Factorial: 1')
        elif x.is_integer():
            while i<x:
                factorial = x*i
                i = i+1
            else:
                return(factorial)
        else:
            return(f'Invalid input: must be an integer value.')

print(Solution().Factorial())
            
            