weight = int(input('ENTER your Weight : '))
lork = input('is this L(pounds) or K(kilograms) : ').upper()

if lork == 'K':
    print(f'Your Weight in Pounds is {weight*2.20462}')
elif lork == 'L':
    print(f'Your Weight in Kilograms is {weight * 0.453592}')
else:
    print('Restart Process Again')
