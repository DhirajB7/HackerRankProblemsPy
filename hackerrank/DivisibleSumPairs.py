lc, k = list(map(lambda a: int(a), input().split(' ')))
lis = list(map(lambda a: int(a), input().split(' ')))
answer = 0
for i in range(0, lc):
    for j in range(i + 1, lc):
        if (lis[i] + lis[j]) % k == 0:
            answer += 1
print(answer)
