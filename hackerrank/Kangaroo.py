x1, v1, x2, v2 = list(map(int, input().split(' ')))
if x1 == x2:
    if v1 == v2:
        print('YES')
    else:
        print('NO')
else:
    if v2 >= v1:
        print('NO')
    else:
        while x1 < x2:
            x1 += v1
            x2 += v2
        if x1 == x2:
            print('YES')
        else:
            print('NO')
