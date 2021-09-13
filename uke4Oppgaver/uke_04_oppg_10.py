#printer tid i sekunder og temperatur i grader celsius for hvert sekund som går.
startingTemp = float(25)
tempIncrease = float(0.625)
boiling = float(100)
time = int(0)
temperature = startingTemp

while temperature < boiling:
    roundedTemperature = round(temperature, 1)
    print(f'{time}s = {roundedTemperature}°C')
    time = time + 1
    temperature = temperature + tempIncrease
print(f'{temperature}°C i {time} sekunder')
