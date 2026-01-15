#Activity Python 2: Task 2
# File: ACT_Python_2p2_secenah.py 
# Date:    10/17/2025
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
# This script determines if a solution is acidic, neutral, or basic.

import math

class Solution:
    def pH(self, x: float):
        if x<0 or x>14:
            return('pH is invalid')
        elif x==7:
            return('neutral')
        elif x>=0 and x<7:
            return('acidic')
        elif x>7 and x<=14:
            return('basic')

x = float(input(f'Input your pH value: '))
print(f'Solution: {Solution().pH(x)}')