#program som konverterer et binært tall til et heltall

binaryNumber = input('Binært tall: ')
number = 0
for digits in binaryNumber:
    number = number * 2 + int(digits)
print(f'{number}')