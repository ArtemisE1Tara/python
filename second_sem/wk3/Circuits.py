# Week 3: Task 2
# File: Circuits.py
# Date:    01/29/2026
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
# This script calculates the total resistance of resistors in parallel and series.

class Solution:
    def Circuits(self, numResistor, config):
        resistorValues = []
        for i in range(numResistor):
            x = float(input(f"Enter resistor {i} value: "))
            while x<0:
                x = float(input(f"Resistor {i} value must be positive.\nEnter resistor {i} value: "))
            resistorValues.append(x)
        # 0=series
        if config == 0:
            R_total = sum(resistorValues)
            print(f"Total resistance: {R_total}")
        
        # 1=parallel
        if config == 1:
            fracList = []
            for x in range(len(resistorValues)):
                fraction = 1/resistorValues[x]
                fracList.append(fraction)
            R_total = 1/sum(fracList)
            print(f"Total resistance: {R_total}")

#call the function
Solution().Circuits(3,1)