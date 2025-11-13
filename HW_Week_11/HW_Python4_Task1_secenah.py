# HW Week 11: --> Task 1
# File: HW_Python4_Task1_secenah.py
# Date:    11/12/2025
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
# This script estimates the value of pi.

#get imports
import random
import math

#get user inputs
num = float(input("Enter how many random points you want to generate: "))
#initialize variables
x = 0
y = 0
point_in = 0
point_total = 0

#input checks
if num<0:
    print("Invalid input. Must be a positive integer.")
    exit()
elif not num.is_integer():
    print("Invalid input. Must be a positive integer.")
    exit()
else:
    #setup for loop
    for i in range(0, int(num), 1):
        #generate random points
        x = random.random()
        y = random.random()
        #update counters
        if (x**2)+(y**2) <= 1:
            point_in = point_in + 1
        point_total = point_total + 1
    #estimate pi and find the difference
    piEst = (point_in/point_total)*4
    difference = abs(piEst-math.pi)
    #print outputs
    print(f"Estimated value of pi: {piEst}\nDifference: {difference}")