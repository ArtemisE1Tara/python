# Week 3 HW: Task 1
# File: Algebra.py
# Date:    02/02/2026
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
# This script computes unique solutions for x and y given 6 numerical inputs.

def Algebra(a1, b1, c1, a2, b2, c2):
    if (a1*b2)-(a2*b1)!=0:

        y = ((a2*c1)-(a1*c2))/((a2*b1)-(a1*b2))
        x = ((b2*c1)-(b1*c2))/((a1*b2)-(a2*b1))

        return(f"y = {y}\nx = {x}")
    
    else:
        return("No unique solutions for x and y.")


