# Activity Python 1: Task 1
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
# This script computes Gam, p and q in relation to speeds of light and mobile objects.

import math

# get inputs
c = float(input("Speed of light, c in m/s: "))
v = float(input("Enter the speed of the mobile, v in m/s: "))
m = float(input("Enter the mass of the mobile, m in kg: "))

class Solution:
    def calculator(self):

        # compute the variables
        Gam = 1/(math.sqrt(1-((v/c)**2)))
        p = m*v
        q = m*v*Gam

        # return statement
        return(f'Gam = {Gam:0.3}\np = {p:.2e}kg*m/s\nq = {q:.2e}kg*m/s')

print(Solution().calculator())
