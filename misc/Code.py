import math
A = float(input('Angle A = '))
B = float(input('Angle B = '))
a = float(input('Side a = '))
C = 180 - A - B
c = a*math.sin(C)/math.sin(A)
b = a*math.sin(B)/math.sin(A)
print('Angle C = {0}'.format(C))
print('Side c = {0}'.format(c))
print('Side b = {0}'.format(b))
input('Press any key to continue.')