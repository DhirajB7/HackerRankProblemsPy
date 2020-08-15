xStart = int(input('x start : '))
xEnd = int(input('x end : '))

yStart = int(input('y start : '))
yEnd = int(input('y end : '))

for x in range(xStart, xEnd + 1):
    for y in range(yStart, yEnd + 1):
        print(f'{x, y}')
