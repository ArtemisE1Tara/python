# Python 2: Conditional Flow Task 2
# File: HW_Python2_Task2_secenah.py 
# Date:    10/22/2025
# By:      Ahmed Secen
# Section: 018
# Team: 2
# 
# ELECTRONIC SIGNATURE
# Ahmed Secen
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# This script determines the category that the 
# blood tests that the user inputs, put the patient in (Normal, High Risk, or Diabetic).

import math

#define user inputs
blood_glucose = float(input("Enter the fasting blood glucose level: "))
hemoglobin = float(input("Enter the hemoglobin A1c level as a percentage without the sign: "))
class Solution:
    #define method for categorizing based on fasting blood glucose levels
    def calcBloodGlucose(self):
        #checks for negative numbers
        if blood_glucose<0:
            return('Invalid fasting blood glucose value')
        elif hemoglobin<0:
            return('Invalid hemoglobin A1c level')
        #sets categories to integers for comparison purposes
        else:
            if blood_glucose<100:
                bloodCategory = 0
            elif blood_glucose>=100 and blood_glucose<=125:
                bloodCategory = 1
            else:
                bloodCategory = 2
            #returns the category number
            return(int(bloodCategory))
        
    #define method for categorizing based on hemoglobin A1c levels
    def calcHemoglobin(self):
        #checks for negative numbers
        if blood_glucose<0:
            return('Invalid fasting blood glucose value')
        elif hemoglobin<0:
            return('Invalid hemoglobin A1c level')
        #sets categories to integers for comparison purposes
        else:
            if hemoglobin<5.7:
                hemoglobinCategory = 0
            elif hemoglobin>=5.7 and hemoglobin<=6.4:
                hemoglobinCategory = 1
            else:
                hemoglobinCategory = 2
            #returns the category number
            return(int(hemoglobinCategory))

#class for determining order of precedence for risk severity
class Precedence: 
    def determinePrecedence(self):
        #checks if the blood glucose level category is greater based on the integer value
        if int(Solution().calcBloodGlucose()) > int(Solution().calcHemoglobin()):
            #redefines the risk categories as strings
            if int(Solution().calcBloodGlucose()) == 0:
                final = 'Normal'
                return(final)
            elif int(Solution().calcBloodGlucose()) == 1:
                final = 'High Risk'
                return(final)
            elif int(Solution().calcBloodGlucose()) == 2:
                final = 'Diabetic'
                return(final)
        #checks if the hemoglobin A1c category is greater based on the integer value
        else:
            if int(Solution().calcHemoglobin()) > int(Solution().calcBloodGlucose()):
                #redefines the risk categories as strings
                if int(Solution().calcHemoglobin()) == 0:
                    final = 'Normal'
                    return(final)
                elif int(Solution().calcHemoglobin()) == 1:
                    final = 'High Risk'
                    return(final)
                elif int(Solution().calcHemoglobin()) == 2:
                    final = 'Diabetic'
                    return(final)
            
#prints the output of 'precedence' as a string
print(f'Patient is: {Precedence().determinePrecedence()}')
            
            

        
