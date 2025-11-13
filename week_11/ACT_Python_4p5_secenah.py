import math

x = float(input('Enter a number: '))
series = 0
for i in range(1, int(x)+1, 1):
    series = 4*((-1**x)/((2*x)+1))
accuracy = math.pi - series
print(f"Final value: {series}\nAccuracy: {accuracy}")
