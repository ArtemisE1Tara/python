# Python 2: Conditional Flow Task 1
# File: HW_Python2_Task1_secenah.py 
# Date:    10/17/2025
# By:      Ahmed Secen
# Section: 018
# Team: 2
# 
# ELECTRONIC SIGNATURE
# Ahmed Secen
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This script determines the stopping sight distance, S, in feet, of how far 
# a driver must be able to see in order to be able to come
# to a complete stop in the event of a hazard in the road

import math

#define user inputs as floats
V = float(input('Input vehicle speed in mph: '))
f = float(input('Input coefficient of friction: '))
G = float(input('Input grade: '))
T_r = float(input('Input reaction time in seconds: '))
#define incline as a string 
incline = str(input('Input direction of incline (-)=downhill and (+)=uphill: '))
class Solution:
    #define method for when the driver is going downhill
    def distanceDownhill(self):
        #checks for invalid values
        if V<0 or V>200:
            return('Invalid speed')
        elif f<0 or f>1:
            return('Invalid coefficient of friction')
        elif G<0 or G>0.5:
            return('Invalid grade')
        elif T_r<0:
            return('Invalid reaction time')
        else:
            S = (
                round((((V**2)/(29.84*(f-G))) + (1.4678*V*T_r)), 3) #round to 3 decimal places
            )
            return(f'Stopping distance: {S}ft')
            
    #define method for when the driver is going uphill
    def distanceUphill(self): 
        #checks for invalid values
        if V<0 or V>200:
            return('Invalid speed')
        elif f<0 or f>1:
            return('Invalid coefficient of friction')
        elif G<0 or G>0.5:
            return('Invalid grade')
        elif T_r<0:
            return('Invalid reaction time')
        else:
            S = (
                round((((V**2)/(29.84*(f+G))) + (1.4678*V*T_r)), 3) #round to 3 decimal places
            )
            return(f'Stopping distance: {S}ft')

    #define method for determining which equation to use based on incline
    def incline(self, incline: str):
        if incline=='-':
            return(Solution().distanceDownhill())
        elif incline=='+':
            return(Solution().distanceUphill())
        else:
            return('Invalid incline direction')
        
#print output result with 'incline' as an argument
print(Solution().incline(incline))

