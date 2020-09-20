lc, left = list(map(int, input().split(' ')))
al = list(map(int, input().split(' ')))
charged = int(input())
al.remove(al[left])
actual = sum(al) // 2
if charged == actual:
    print('Bon Appetit')
else:
    print(charged-actual)
