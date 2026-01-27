# HW1: Task 1
# File: HW1_Task1_secenah.py
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
# This script determines the percentage of reliability simulations failed.

#get imports
import random

#define class
class Solution:
    #define method
    def Reliability(self):
        #get inputs
        simNum = int(input("Enter simulation count: "))
        while simNum<=0:
            simNum = int(input("Invalid input. Simulation count must be greater than zero.\nEnter simulation count: "))
        
        processNum = int(input("Enter component process count: "))
        while processNum<=0:
            processNum = int(input("Invalid input. Component process count must be greater than zero.\nEnter component process count: "))
        
        #initialize reliability list
        compRel = []

        #set loop for entering reliability values
        for i in range(1, processNum+1):
            Rel = float(input(f"Enter reliability of component {i}: "))

            while Rel<0 or Rel>1:
                Rel = float(input(f"Invalid input. Reliability must be in range 0-1.\nEnter reliability of component {i}: "))
            else:
                compRel.append(Rel)
        
        #initialize fail counter
        failCount = 0
        #setup loop for simulation runs
        for x in range(simNum+1):
            simFail = 0
            #iterate through reliability values
            for y in range(len(compRel)):
                if compRel[y]<random.random():
                    simFail = 1
            if simFail == 1:
                #update fail counter
                failCount = failCount + 1
        #caluclate failure rate percentage
        percentFail = (failCount/simNum)*100
        #print output
        print(f"{percentFail}% of simulations failed.")

#run program
Solution().Reliability()