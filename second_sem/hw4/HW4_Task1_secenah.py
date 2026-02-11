# Week 4 HW: Task 1
# File:    HW4_Task1_secenah.py
# Date:    02/10/2026
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
# This script reads corresponding dates, energy amounts, and prices, then writes a new file and adds a column for total energy expenditure.

import os
# generalize file paths

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'HW4_Task1.txt')
output_path = os.path.join(script_dir, 'OhioEnergy_secenah.txt')

dateList = [] 
consumptionList = [] #Billions of BTUs
energyPrice = [] #dollars per million BTU

convertedPrice = [] #dollars per BILLION BTU

totalExpenditureList = []

with open(file_path, 'r') as file:
    for line in file:
        #seperate data
        parts = line.strip().split()

        date = parts[0]
        consumption = float(parts[1])
        price = float(parts[2])
        

        # append data to two lists
        dateList.append(date)
        consumptionList.append(consumption)
        energyPrice.append(price)

# convert prices    
for i in energyPrice:
    newPrice = i*1000
    convertedPrice.append(newPrice)

#compute total expenditure to date
for i in range(len(dateList)):
    total = sum(convertedPrice[:i])
    totalExpenditureList.append(total)

#write to new file
with open(output_path, 'w') as new:
    for i in range(len(dateList)):
        new.write(f"{dateList[i]}\t{consumptionList[i]}\t{energyPrice[i]}\t{totalExpenditureList[i]}\n")
    

