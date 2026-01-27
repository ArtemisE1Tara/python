import random

class Solution:
    def Reliability(self):
        simNum = int(input("Enter simulation count: "))
        while simNum<=0:
            simNum = int(input("Invalid input. Simulation count must be greater than zero.\nEnter simulation count: "))
        
        processNum = int(input("Enter component process count: "))
        while processNum<=0:
            processNum = int(input("Invalid input. Component process count must be greater than zero.\nEnter component process count: "))
        
        compRel = []
        for i in range(1, processNum+1):
            Rel = float(input(f"Enter reliability of component {i}: "))

            while Rel<0 or Rel>1:
                Rel = float(input(f"Invalid input. Reliability must be in range 0-1.\nEnter reliability of component {i}: "))
            else:
                compRel.append(Rel)
        
        failCount = 0
        for x in range(simNum+1):
            simFail = 0
            for y in range(len(compRel)):
                if compRel[y]<random.random():
                    simFail = 1
            if simFail == 1:
                failCount = failCount + 1
        
        percentFail = (failCount/simNum)*100

        print(f"{percentFail}% of simulations failed.")

Solution().Reliability()