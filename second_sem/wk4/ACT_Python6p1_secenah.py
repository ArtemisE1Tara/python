# Week 4 CFU: Task 1
# File: ACT_Python6p1_secenah.py
# Date:    02/05/2026
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
# This script reads celsius temperatures from a text file, converts each value to Fahrenheit, then saves the new temperatures to a new text file.

import os

# generalize file paths
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'TempC.txt')
output_path = os.path.join(script_dir, 'TempF.txt')

# Read temps from file
with open(file_path, 'r') as file:
    content = file.readlines()

# Convert celsius to new temp
floatList = [float(temp.strip()) for temp in content]
newTemp = []
for tempC in floatList:
    tempF = round(((tempC * 1.8) + 32))
    newTemp.append(tempF)

# Write new temps to file
with open(output_path, 'w') as new:
    for i in newTemp:
        new.write(f"{i}\n")