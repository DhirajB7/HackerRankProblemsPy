from collections import Counter

lc = int(input())
lis = list(map(lambda x: int(x), input().split(' ')))
lis.sort()
birds = Counter(lis)
print(birds.most_common(1)[0][0])