# Activity Python 1: Task 3
# File: ACT_Python_1p3B_secenah.py
# Date:    10/3/2025
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
# This script computes the maximum allowable sound intensity given the user's inputs.

import math

SPL = float(input("Enter the maximum allowable SPL in (Db): "))
P_Ref = float(input("Enter the reference pressure in (Pa): "))
v = float(input("Enter the particle velocity in (m/s): "))

P = P_Ref*(math.pow(10,(SPL/20)))

I = v*P

print('Maximum allowable sound intensity (I): {0:0.2f} W/m^2' .format(I))