# HW1: Task 2
# File: HW1_Task2_secenah.py
# Date:    01/27/2026
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
# This script determines if a process is in control based on whether 
# or not each sample range average is iwthin upper and lower control limits.

#get imports
import math

#hardcode sample value 2D list
List = [[0.04, -0.01, 0.03, 0.02, 0.03], 
        [0.02, 0.01, 0.03, -0.01, 0.00], 
        [0.06, 0.07, -0.03, 0.05, 0.04],
        [-.02, -0.03, 0.01, 0.03, 0.02]]

#hardcode variable value
A = 0.557

#initialize sample averages list
avgSumList = []

#computes averages
X1 = sum(List[0])/len(List[0])
X2 = sum(List[1])/len(List[1])
X3 = sum(List[2])/len(List[2])
X4 = sum(List[3])/len(List[3])

#compute average of averages
x_avg = (X1+X2+X3+X4)/4

#compute sample value ranges
R1 = max(List[0])-min(List[0])
R2 = max(List[1])-min(List[1])
R3 = max(List[2])-min(List[2])
R4 = max(List[3])-min(List[3])

#compute average of sample value ranges
R_avg = (R1+R2+R3+R4)/4

#compute upper and lower control limits
UCL = x_avg + (A*R_avg)
LCL = x_avg - (A*R_avg)

#set initial booleans to False
X1_pass = False
X2_pass = False
X3_pass = False
X4_pass = False

#check if sample averages are within limits
if X1<UCL and X1>LCL:
    X1_pass = True

if X2<UCL and X2>LCL:
    X2_pass = True

if X3<UCL and X3>LCL:
    X3_pass = True

if X4<UCL and X4>LCL:
    X4_pass = True

#check if whole process is in control
if X1_pass==X2_pass==X3_pass==X4_pass:
    print("Process is in control.")
else:
    print("Process is out of control.")



    

