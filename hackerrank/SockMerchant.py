lc = int(input())
al = list(map(int, input().split(' ')))
dc = {}
answer = 0
for i in al:
    if i in dc:
        dc.__setitem__(i, dc.get(i) + 1)
    else:
        dc.__setitem__(i, 1)
for i in dc.values():
    answer += i // 2
print(answer)