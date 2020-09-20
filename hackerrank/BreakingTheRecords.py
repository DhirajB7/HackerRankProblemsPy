int(input())
lis = list(map(lambda a: int(a), input().split(' ')))
minScore = lis[0]
minScoreCount = 0
maxScore = lis[0]
maxScoreCount = 0
for i in lis:
    if i < minScore:
        minScore = i
        minScoreCount += 1
    if i > maxScore:
        maxScore = i
        maxScoreCount += 1
print(f'{maxScoreCount} {minScoreCount}')
