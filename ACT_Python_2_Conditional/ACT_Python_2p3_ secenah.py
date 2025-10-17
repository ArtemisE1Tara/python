#Activity Python 2: Task 3
# File: ACT_Python_2p3_secenah.py 
# Date:    10/17/2025
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
# This script computes the equivalent spring constant and total displacement as well as the force and displacement for
# each spring for both parallel and series configurations.

class Solution:
    def Series(self):
        if K1<0:
            return('invalid K1 input')
        elif K2<0:
            return('invalid K2 input')
        elif F_total<0:
            return('invalid F_total input')
        else: 
            K_eq = K1+K2
            F_1 = F_total
            F_2 = F_total
            x_1 = (
                F_1/K1
            )
            x_2 = (
                F_2/K2
            )
            xTotal = (
                x_1+x_2
            )
            return(
                f'Displacement 1: {x_1}m\n'
                f'Displacement 2: {x_2}m\n'
                f'Total Displacement: {xTotal}m\n'
                f'Force 1: {F_1}N\n'
                f'Force 2: {F_2}N\n'
                f'Keq: {K_eq}N/m'
            )
        
    def Parallel(self):
        if K1<0:
            return('invalid K1 input')
        elif K2<0:
            return('invalid K2 input')
        elif F_total<0:
            return('invalid F_total input')
        else: 
            K_eq = K1+K2
            F_1 = (K1/(K1+K2)) * F_total
            F_2 = (K2/(K1+K2)) * F_total
            x_1 = (
                F_1/K1
            )
            x_2 = (
                F_2/K2
            )
            xTotal = x_1
            return(
                f'Displacement 1: {x_1}m\n'
                f'Displacement 2: {x_2}m\n'
                f'Total Displacement: {xTotal}m\n'
                f'Force 1: {F_1}N\n'
                f'Force 2: {F_2}N\n'
                f'Keq: {K_eq}N/m'
            )
    def configuration(self, config: str):
        if config=='parallel':
            return(Solution().Parallel())
        elif config=='series':
            return(Solution().Series())
        
K1 = float(input('Input K1: '))
K2 = float(input('Input K2: '))
F_total = float(input('Input total force: '))
config = str(input('Input spring system type (series or parallel): '))

print(Solution().configuration(config))



