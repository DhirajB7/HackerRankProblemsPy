lc = int(input())
al = list(map(int, input().split(' ')))
al.sort()
last = al[-1]
print(al.count(last))
