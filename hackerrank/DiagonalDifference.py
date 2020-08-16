import math

lc = int(input())
mat = []

for i in range(lc):
    mat.append(list(map(lambda x: int(x), input().split(' '))))

primaryDiagnoal = sum([mat[x][x] for x in range(lc)])
secondaryDiagnol = sum([mat[x][lc-x-1] for x in range(lc)])

print(int(math.fabs(primaryDiagnoal - secondaryDiagnol)))
