# Activity Python 1: Task 2
# File: ACT_Python_1p2_secenah.py 
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
# This script calculates the Reynolds number given the user's inputs.


import math

V = (float(input('Enter the fluid velocity in mi/hr: ')))/2.237 #convert to m/s
L = float(input('Enter the typical length in (in): ' ))/39.37 #convert to meters
mu = float(input('Enter the dynamic viscosity of the fluid in (lb/(in*s)): '))*17.857 #convert to kg/(m*s)
den = float(input('Enter density of the fluid in (lb/in^3): '))*27679.9 #convert to kg/m^3

Re = (den*V*L)/mu

print('Reynolds number: {0:0.2f}' .format(Re))



