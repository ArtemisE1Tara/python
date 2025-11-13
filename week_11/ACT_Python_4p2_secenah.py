# Week 11: --> Task 2
# File: ACT_Python_4p2_secenah.py
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
# This script calculates the factorial of a number.

#get inputs
x = float(input("Enter a number to find the factorial of: "))
#initilaize variables
factorial = 1
#check conditions
if x<0:
    print("Invalid input: must be a positive number.")
elif x==0:
    print(f"{x}! = 1")
elif not x.is_integer():
    print("Invalid input: number must be an integer.")
elif x.is_integer():
    #set loop conditions
    for num in range(1, int(x)+1, 1):
        factorial = factorial*num
    #output factorial
    print(f"{x}! = {factorial}")