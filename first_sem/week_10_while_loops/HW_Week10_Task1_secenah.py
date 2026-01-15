#HW - Week 10: Python (While Loops) --> Task 1
# File: HW_Week10_Task1_secenah.py
# Date:    11/05/2025
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
# This script models Newton's Law of Cooling.

import math

#get user inputs
try:
    T_0 = float(input("Enter the initial temperature in °C: "))
    T_s = float(input("Enter the surrounding temperature °C: "))
    k = float(input("Enter the heat transfer coefficient: "))
except ValueError:
    print("Invalid input: please enter a number.")
    exit()

#initialize variables
change = 0.5
tolerance = 0.1
t = 0.0 
T_prev = T_0 
T_current = T_0
temp_change = tolerance + 1.0 

#set while condition
while temp_change >= tolerance:
    #update variables
    t = t + change
    T_current = T_s + (T_0 - T_s)*math.exp(-k*t)
    temp_change = T_prev-T_current
    T_prev = T_current 

#print outputs
print(f"Final temperature: {T_current:.2f}°C")
print(f"Time taken: {t:.1f} seconds")

