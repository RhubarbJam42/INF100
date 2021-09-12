#printer tid i sekunder og temperatur i grader celsius for hvert sekund som går.
startingTemp = float(25)
tempIncrease = float(0.625)
boiling = float(100)
time = int(0)
temperature = startingTemp

while temperature < boiling:
    print(f'{time}s = {temperature}°C')
    time = time + 1
    temperature = temperature + tempIncrease
print(f'{temperature}°C i {time} sekunder')
