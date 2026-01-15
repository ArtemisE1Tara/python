# PYTHON 3: REPETITION FLOW (CONDITIONAL STRUCTURES) --> Task 3
# File: ACT_Python_3p3_secenah.py
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
# This script calculates the number who's factorial is closest to the given number 
# and the difference between that number's factorial and the given number.

import math

x = float(input("Enter a number: "))

class Solution:
    def Factorial(self):
        i = 1
        factorial = 1
        previous_factorial=1
        previous_i = 0
        difference = 0
        if x<0:
            return('Invalid input: must be a positive value')
        elif x==0:
            return('Factorial: 1')
        elif x.is_integer():
            while factorial<=x:
                previous_i = i
                previous_factorial = factorial
                i = i+1
                factorial = factorial*i
            else:
                difference = x-previous_factorial
                return(f'Number whos factorial is closest to {x}: {previous_i}\nFactorial of {previous_i}: {previous_factorial}\nDifference between {x} and {previous_factorial}: {difference}') 
        else:
            return(f'Invalid input: must be an integer value.')

print(f'{Solution().Factorial()}')