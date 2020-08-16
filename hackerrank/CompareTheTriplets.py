a = list(map(lambda x: int(x), input().split(' ')))
b = list(map(lambda x: int(x), input().split(' ')))
aScore = 0
bScore = 0
for i in range(len(a)):
    if a[i] > b[i]:
        aScore += 1
    elif a[i] < b[i]:
        bScore += 1
print(f'{aScore} {bScore}')
