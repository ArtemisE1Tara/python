from HW3_Task3_secenah import ConvertDistance

x = float(input("Initial measurement: "))
y = str(input("Available starting units:\nin\nft\ncm\nm\nyd\nEnter one: "))
z = str(input("Available ending units:\nin\nft\ncm\nm\nyd\nEnter one: "))

print(ConvertDistance(x, y, z))