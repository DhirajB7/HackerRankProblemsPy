numbers = [2, 2, 4, 6, 3, 4, 6, 1]
unique = []
for i in numbers :
    if i not in unique:
        unique.append(i)
unique.sort()
print(unique)
