# Activity Python 1: Task 2
# File: ACT_Python_Task2_secenah.py
# Date:    01/15/2026
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
# This script detemines the state of a substance based on temperature and pressure.
import math

# get inputs
P = float(input("Enter the pressure in atm: "))
T_C  = float(input("Enter the temperature in celsius: "))

class Solution:
    def calculator(self):
        #convert temperature to kelvin
        T = T_C+273.15

        # compute variables
        P1 = 0.006*math.exp(((6293*((1/273.15)-(1/T)))-(0.56*math.log(T/273.15))))
        P2 = 0.006*math.exp(((6808*((1/273.15)-(1/T)))-(5.09*math.log(T/273.15))))
        
        # setup conditions
        if T>647 and P>218:
            return("Super critical liquid")
        else:
            if T<273.15:
                if P>P1:
                    return("Solid/Ice")
                else:
                    return("Gas/Vapor")
            else:
                if P>P2:
                    return('Liquid/Water')
                else:
                    return("Gas/Vapor")

print(Solution().calculator())




