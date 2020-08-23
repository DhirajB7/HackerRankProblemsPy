import math
for i in range(int(input())):
    catA, catB, mouse = list(map(int, input().split(' ')))
    catAMouse = math.fabs(catA - mouse)
    catBMouse = math.fabs(catB - mouse)
    if catAMouse > catBMouse:
        print('Cat B')
    elif catAMouse < catBMouse:
        print('Cat A')
    else:
        print('Mouse C')
