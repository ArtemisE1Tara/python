# Week 4 HW: Task 2
# File:    HW4_Task2_secenah.py
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
# This script reads corresponding columns of data, computes the pressure if the temperature is in range, then writes them to a new file.

import os

#generalize imports
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'HW4_Task2.txt')
output_path = os.path.join(script_dir, 'Task2_Results_secenah.txt ')

#initialize lists
substanceList = []
Temperature = []
T_min = []
T_max = []
Pressure = []
A_list = []
B_list = []
C_list = []

#opens data file in read mode
with open(file_path, 'r') as file:
    next(file)
    for line in file:
        #seperate data
        parts = line.strip().split()

        substance = parts[0]
        temp = float(parts[6])
        t_min = float(parts[4])
        t_max = float(parts[5])
        a_list = float(parts[1])
        b_list = float(parts[2])
        c_list = float(parts[3])

        # append data to two lists
        substanceList.append(substance)
        Temperature.append(temp)
        T_min.append(t_min)
        T_max.append(t_max)
        A_list.append(a_list)
        B_list.append(b_list)
        C_list.append(c_list)

#computes pressure
for i in range(len(substanceList)):
    if Temperature[i]>=T_min[i] and Temperature[i]<=T_max[i]:
        P = 10**(A_list[i]-(B_list[i]/(C_list[i]+Temperature[i])))
        Pressure.append(P)
    #output error
    else:
        Pressure.append(-9999.00)

#write new file
with open(output_path, 'w') as new:
    new.write(f"Substance\tT\tP\n")
    for i in range(len(substanceList)):
        new.write(f"{substanceList[i]:15}\t{Temperature[i]:10}\t{Pressure[i]:10.2f}\n")
    

