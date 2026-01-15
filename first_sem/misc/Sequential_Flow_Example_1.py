import math

mass = float(input('Input your mass in kilograms: '))
radius = float(input('Input your radius in meters: '))

gConstant = float(
    6.67*(math.pow(10,-11))
)

g = float(
    (gConstant*mass)/radius**2
)

g@gms = 352

print('{0:0.2f}' .format(g))