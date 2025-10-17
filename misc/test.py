import math

x = float(input('Test value: '))    
if x>1:
    print("Hello World")
elif x==1:
    y = round((float(math.log((x+4)))),4)
    print(f'{y}')
else:
    print('Under construction')