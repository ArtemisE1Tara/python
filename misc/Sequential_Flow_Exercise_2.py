import math

x_1 = float(input('First x-value: '))
y_1 = float(input('First y-value: '))

x_2 = float(input('Second x-value: '))
y_2 = float(input('Second y-value: '))

firstValue = x_2-x_1
secondValue = y_2-y_1

distance = float(
    math.sqrt(
        math.pow(firstValue, 2)+math.pow(secondValue, 2)
    )
)

print('{0:0.3f}' .format(distance))
