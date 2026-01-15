import math
A = int(input('Angle A = '))
B = int(input('Angle B = '))
a = float(input('Side a = '))
C = 180 - A - B
c = a*math.sin(C)/math.sin(A)
b = a*math.sin(B)/math.sin(A)
print('Angle C = {C}')
print('Side c = {0}'.format(c))
print('Side b = {b}')

