# Week 3 HW: Task 2
# File: ConvertDistance.py
# Date:    02/02/2026
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
# This script converts a measurement to inches, feet, centimeters, or meters, and vice versa.

def ConvertDistance(initialMeasurement, unitStart, unitEnd):
    lookUp = [
        [1, 1/12, 2.54, 0.0254],
        [12, 1, 30.48, 0.3048],
        [1/2.54, 1/30.48, 1, 1/100],
        [1/0.0254, 1/0.3048, 100, 1]
    ]

    unitName = ["in", "ft", "cm", "m"]
    
    # could also define variables for readability, but it's cool to see all the logic in one line
    # y = unitName.index(unitStart)
    # x = unitName.index(unitEnd)
    convertedNum = initialMeasurement * lookUp[unitName.index(unitStart)][unitName.index(unitEnd)]
    return(convertedNum)
