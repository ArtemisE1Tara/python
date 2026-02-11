# Week 4 CFU: Task 2
# File: ACT_Python6p2_secenah.py
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
# This script reads the amount of a snowfall 

import os
# generalize file paths

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'Snow_Fall.txt')
# initialize lists
dateList = []
heightList = []
# open file
with open(file_path, 'r') as file:
    for line in file:
        #seperate data
        parts = line.strip().split()
        date = parts[0]
        height = float(parts[1])
        # append data to two lists
        dateList.append(date)
        heightList.append(height)
maxSnow = round((max(heightList)), 2)
maxDate = dateList[heightList.index(maxSnow)]
# output
print(f"{maxSnow} inches on {maxDate}")
