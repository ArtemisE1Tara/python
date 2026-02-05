import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'TempC.txt')
output_path = os.path.join(script_dir, 'TempF.txt')

# Read temps from file
with open(file_path, 'r') as file:
    content = file.readlines()

# Convert celsius to new temp
floatList = [float(temp.strip()) for temp in content]
newTemp = []
for tempC in floatList:
    tempF = round(((tempC * 1.8) + 32))
    newTemp.append(tempF)

# Write new temperatures to file
with open(output_path, 'w') as new:
    for i in newTemp:
        new.write(f"{i}\n")