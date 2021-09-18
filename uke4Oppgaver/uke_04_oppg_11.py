#programmet beregner hvor lang tid det tar en stein å nå bakken fra en gitt høydeposisjon
startPosition = float(input('Stenen droppes fra høyde: '))
time = float(0)
position = (startPosition - 1.0 / 2.0 * 9.8 * time ** 2.0)
landed = 0

while position > 0:
    position = round(position, 2)
    print(f'{position} m')
    time = time + 1.0
    position = (startPosition - 1.0 / 2.0 * 9.8 * time ** 2.0)

time = int(time)
print(f'{landed} m')
betweenTime = int(time - 1)
print(f'Stenen lander mellom {betweenTime} og {time} sekunder etter at den droppes.')
