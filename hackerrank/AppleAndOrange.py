s, t = list(map(int, input().split(' ')))
a, b = list(map(int, input().split(' ')))
m, n = list(map(int, input().split(' ')))
ml = list(map(int, input().split(' ')))
nl = list(map(int, input().split(' ')))
ac, oc = [0, 0]
for i in ml:
    if s <= a + i <= t:
        ac += 1
for i in nl:
    if s <= b + i <= t:
        oc += 1
print(ac)
print(oc)