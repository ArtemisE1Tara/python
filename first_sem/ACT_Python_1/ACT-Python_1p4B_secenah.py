# Activity Python 1: Task 4
# File: ACT-Python_1p4B_secenah.py 
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
# This script computes the heat transfer in a building relative to the outside temperature given the user's inputs.

import math

T_H = (
    (((float(input('Enter the interior temperature in (F): '))-32)*5)/9)+273.15 #convert to kelvin
)

T_Out = (
    (((float(input('Enter the exterior temperature in (F): '))-32)*5)/9)+273.15 #convert to kelvin
)

A = (float(input('Enter the surface area of the house in (ft^2): ')))/10.764 #convert to m^2

L = (float(input('Enter the height of the house in (ft): ')))/3.281 #convert to meters

Ra = (
    float((9.81*(1/T_Out)*(T_H-T_Out)*(math.pow(L,3))*0.7)/(math.pow(1.271e-5,2)))
)

Nu = float((0.59*(math.pow(Ra, 0.25)))/0.25)

h = float((Nu*0.25)/L)

Q = h*A*(T_H-T_Out)

print('Heat transfer rate: {0:0.2f} W' .format(Q))




