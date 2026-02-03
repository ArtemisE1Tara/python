# Week 3 HW: Task 3
# File: HW3_Task3_secenah.py
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
# This script converts a measurement to inches, feet, centimeters, meters, yards, and vice versa.

def ConvertDistance(initialMeasurement, unitStart, unitEnd):
    lookUp = [
        # add support for yards
        [1, 1/12, 2.54, 0.0254, 1/36],
        [12, 1, 30.48, 0.3048, 1/3],
        [1/2.54, 1/30.48, 1, 1/100, 1/91.44],
        [1/0.0254, 1/0.3048, 100, 1, 1/0.9144],
        [36, 3, 91.44, 0.9144, 1],
    ]

    unitName = ["in", "ft", "cm", "m", "yd"]
    
    # could also define variables for readability, but it's cool to see all the logic in one line
    # y = unitName.index(unitStart)
    # x = unitName.index(unitEnd)
    convertedNum = initialMeasurement * lookUp[unitName.index(unitStart)][unitName.index(unitEnd)]
    return(f"Result: {convertedNum}{unitEnd}")

# sample usage
# from HW3_Task3_secenah import ConvertDistance

# x = float(input("Initial measurement: "))
# y = str(input("Available starting units:\nin\nft\ncm\nm\nyd\nEnter one: "))
# z = str(input("Available ending units:\nin\nft\ncm\nm\nyd\nEnter one: "))

# print(ConvertDistance(x, y, z))
