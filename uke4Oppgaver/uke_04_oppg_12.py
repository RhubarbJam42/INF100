#program som konverterer et binært tall til et heltall

binaryNumber = input('Binært tall: ')
number = 0
for digit in binaryNumber:
    number = number * 2 + int(digit)
print(f'{number}')