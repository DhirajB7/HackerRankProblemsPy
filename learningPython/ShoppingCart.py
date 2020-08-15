prices = [10, 20, 30, 40, 80, 60, 90, 70, 11, 12, 10, 1, 4, 41, 4, 22]

total = 0

for price in prices:
    total += price
    print(f'{price} {total}')

print(total)
