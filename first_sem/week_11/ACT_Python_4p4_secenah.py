# Week 11: --> Task 4
# File: ACT_Python_4p4_secenah.py
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
# This script calculates the Jacobsthal sequence to the n'th term provided by the user.

#get inputs
n = float(input("Enter the n'th term: "))
#define class
class Solution:
    #define method
    def Jacobsthal(self):
        #check conditions
        if n<0:
            return("Invalid input: number must be a positive value")
        elif not n.is_integer():
            return("Invalid input: number must be an integer")
        elif n==0:
            return(f"Jacobsthal number: 0")
        elif n==1:
            return(f"Jacobsthal number: 1")
        elif n.is_integer():
            #initialize variables
            J_0=0
            J_1=1
            #define sequence
            sequence = [0, 1]
            #set loop conditions
            for i in range(2, int(n)+1):
                J_next = J_1+2*J_0
                #append each Jacobsthal number to sequence
                sequence.append(J_next)
                J_0=J_1
                J_1=J_next
            #output sequence
            return(f"Jacobsthal sequence: {sequence}")
print(f"{Solution().Jacobsthal()}")
