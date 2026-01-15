# HW_Week6_Python1: Task 2
# File: HW_Python1_Task2_secenah.py
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
# This script determine the temperature, T (in Celsius), of the liquid in a pipe based on the resistance of the
# thermistor, R, the reference temperature, T_o, the reference Temperature Resistance, R_o, and the
# thermal property of the material, β.

import math

#set user inputs and constants
R = float(input('Enter the resistance of the thermistor at the current temperature (in Ω): '))
beta = 3969 #in kelvin
T_o = 85+273.15 #convert to kelvin
R_o = 1075 #in ohms

#calculate numerator and denominator
denom = T_o*(math.log((R/R_o)))+beta
num = beta*T_o

Temp = round(((num/denom)-273.15), 2) #convert back to celsius and round to two decimal places

print(f'Temperature: {Temp}°C')

