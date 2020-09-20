lc = int(input())
lis = list(map(lambda x: int(x), input().split(' ')))
d, m = list(map(lambda x: int(x), input().split(' ')))
answer = 0
for i in range(0, lc):
    add = sum(lis[i:i + m])
    if add == d:
        answer += 1
print(answer)
