#HW - Week 10: Python (While Loops) --> Task 2
# File: HW_Week10_Task2_secenah.py
# Date:    11/05/2025
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
# This script simulates a pressure safety system.

import math
import random

#get user inputs
readingNum = float(input('Enter the amount of high/low readings: '))
#check if inputs are valid
while readingNum<0 or not readingNum.is_integer():
    print('Invalid input: must be a positive integer value.')
    readingNum = float(input('Enter the amount of high/low readings: '))
#initialize variables
lowPressureCount = 0
highPressureCount = 0
readingCount = 0
#set loop conditions
while lowPressureCount<readingNum and highPressureCount<readingNum:
    #randomize pressure readings
    pressureReading = 200*random.random()+50
    #determine if readings are high or low
    if pressureReading<=75:
        lowPressureCount = lowPressureCount + 1
        readingCount = readingCount + 1
    elif pressureReading>=225:
        highPressureCount = highPressureCount + 1
        readingCount = readingCount + 1
#output results
if lowPressureCount>highPressureCount:
    print(f'System shutdown\nReason: low pressure limit exceeded.\nTotal reading count: {readingCount}\nHigh readings: {highPressureCount}\nLow readings: {lowPressureCount}')
elif lowPressureCount<highPressureCount:
    print(f'System shutdown\nReason: high pressure limit exceeded.\nTotal reading count: {readingCount}\nHigh readings: {highPressureCount}\nLow readings: {lowPressureCount}')
else:
    exit()






