# HW_Week6_Python1: Task 1
# File: HW_Python1_Task1_secenah.py
# Date:    10/6/2025
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
# This script computes the displacement and potential energy of an object.

import math

#set user inputs
A = float(input('Enter the initial displacement of the object in (m): '))
K = float(input('Enter the spring constant in (N/m): '))
M = float(input('Enter the mass of suspended object and spring in (kg): '))
t = float(input('Enter the time in (s): '))

degrees = (
    (math.sqrt(K/M))*t
)

#convert degrees to radians
radians = math.radians(degrees)

p = (
    A*math.cos(degrees) #simple harmonic motion equations should normally use radians but not in this case
                                
)

PE_t = round(0.5*K*(p**2)) #round output to nearest whole number

print(
    f'Potential Energy: {PE_t} J\n',
    f'Displacement: {p:0.1f} m'
)

