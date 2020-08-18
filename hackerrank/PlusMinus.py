def check(data):
    data = str(data)
    if len(data) < 8:
        return data + '0' * (8 - len(data))
    elif len(data) > 8:
        return data[0:9]
    else:
        return data


total = int(input())
al = list(map(int, input().split(' ')))

pos = len(list(filter(lambda x: int(x) > 0, al))) / total
print(check(pos))

neg = len(list(filter(lambda x: int(x) < 0, al))) / total
print(check(neg))

zro = len(list(filter(lambda x: int(x) == 0, al))) / total
print(check(zro))
