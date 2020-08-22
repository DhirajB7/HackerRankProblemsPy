al = list(map(int,input().split(' ')))
al.sort()
print(f'{sum(al[:-1])} {sum(al[1:])}')
