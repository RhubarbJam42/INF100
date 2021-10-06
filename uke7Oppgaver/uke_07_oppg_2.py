# funksjon som tar en streng med én ukes temperaturer og gjør de om til float

def update_weather(temperatures):
    # lager en ny liste som legger til float verdier i listen. Returnerer tuple av listen
    list_of_temperatures = temperatures.split()
    updated_temperature = []
    for item in list_of_temperatures:
        updated_temperature.append(float(item))
    return tuple(updated_temperature)


def tuesday_weather(temperatures):
    #tar inn tuple og gir tilbake index 1
    return float(temperatures[1])

#tester
print(update_weather("16.1 14.1 13.3 15.0 13.0 13.2 12.9"))
#print(tuesday_weather("16.1 14.1 13.3 15.0 13.0 13.2 12.9"))
#print(tuesday_weather((16.1, 14.1, 13.3, 15.0, 13.0, 13.2, 12.9)))
