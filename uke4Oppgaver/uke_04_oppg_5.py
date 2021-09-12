#while-loop som beregner fakultet av et tall
number = int(input('Tall: '))
factorial = 1
while number > 0:
    factorial = factorial * number
    number = number - 1
print(factorial)