import math

List = [[0.04, -0.01, 0.03, 0.02, 0.03], 
        [0.02, 0.01, 0.03, -0.01, 0.00], 
        [0.06, 0.07, -0.03, 0.05, 0.04],
        [-.02, -0.03, 0.01, 0.03, 0.02]]

A = 0.557

avgSumList = []

X1 = sum(List[0])/len(List[0])
X2 = sum(List[1])/len(List[1])
X3 = sum(List[2])/len(List[2])
X4 = sum(List[3])/len(List[3])

x_avg = (X1+X2+X3+X4)/4

R1 = max(List[0])-min(List[0])
R2 = max(List[1])-min(List[1])
R3 = max(List[2])-min(List[2])
R4 = max(List[3])-min(List[3])

R_avg = (R1+R2+R3+R4)/4

UCL = x_avg + (A*R_avg)
LCL = x_avg - (A*R_avg)

X1_pass = False
X2_pass = False
X3_pass = False
X4_pass = False

if X1<UCL and X1>LCL:
    X1_pass = True

if X2<UCL and X2>LCL:
    X2_pass = True

if X3<UCL and X3>LCL:
    X3_pass = True

if X4<UCL and X4>LCL:
    X4_pass = True

if X1_pass==X2_pass==X3_pass==X4_pass:
    print("Process is in control.")
else:
    print("Process is out of control.")



    

