# Week 3: Task 1
# File: Springs.py
# Date:    01/29/2026
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
# This script calculates the equilibrium constant, individual forces on springs (where applicable),
# and total displacement of springs in parallel and series.

def Springs(K1, K2, F_total, config):
    if K1<0:
        return("K1 must be positive.")
    if K2<0:
        return("K2 must be positive.")
    if F_total<0:
        return("Total force must be positive.")
    
    # 0=parallel 
    if config==0:
        #equilibrium constant
        K_eq = K1+K2
        #total distance (x1 and x2 are the same)
        x_total = F_total/K_eq
        #individual spring forces
        F1 = K1*x_total
        F2 = K2*x_total
        return(K_eq, x_total, F1, F2)
    # 1=series
    if config==1:
        #equilibrium constant
        K_eq = (K1*K2)/(K1+K2)
        #F1 and F2 are equal to F_total
        #individual stretch distances
        F1 = F_total
        F2 = F_total
        x1 = F_total/K1
        x2 = F_total/K2
        #total stretch distance
        x_total = x1 + x2
        return(K_eq, x_total, F1, F2)
    
#test case:
#negative_result = Springs(4,-6,69,1)
#positive_result = Springs(4,6,69,1)

#print(f"Bad result: {negative_result}\nGood result: {positive_result}")



