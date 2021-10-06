#funksjon som tar en streng med én ukes temperaturer og gjør de om til float

def update_weather(temperatures):
    #lager en ny liste som legger til float verdier i listen. Returnerer tuple av listen
    list_of_temperatures = temperatures.split(' ')
    updated_temperature = []
    for item in list_of_temperatures:
        updated_temperature.append(float(item))
    return tuple(updated_temperature)

def tuesday_weather(temperatures):
    #splitter strengen om til en liste og returnerer index 1 som er "Tirsdag" 
    list_of_temperatures = temperatures.split(' ')
    return list_of_temperatures[1]

#print(update_weather("16.1 14.1 13.3 15.0 13.0 13.2 12.9"))
#print(tuesday_weather("16.1 14.1 13.3 15.0 13.0 13.2 12.9"))

