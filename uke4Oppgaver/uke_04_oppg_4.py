#sier om et tall er et partall eller oddetall
for number in range(12, 28, 1):
    number = number
    if number % 2 == 0:
        print(number, 'er et partall!')
    else:
        print(number, 'er et oddetall!')