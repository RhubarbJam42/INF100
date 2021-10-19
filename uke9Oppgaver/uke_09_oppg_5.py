# dictionary med informasjon om værstasjoner

weather_stations = {
    "Bergen": {
        "Wind speed": 3.6,
        "Wind direction": "northeast",
        "Precipitation": 5.2,
        "Device": "WeatherMaster500"
    },
    "Trondheim": {
        "Wind speed": 8.2,
        "Wind direction": "northwest",
        "Precipitation": 0.2,
        "Device": "ClimateDiscoverer3000"
    },
    "Svalbard": {
        "Wind speed": 7.5,
        "Wind direction": "southwest",
        "Precipitation": 1.1,
        "Device": "WeatherFinder5.0"
    },
}

for location in weather_stations:
    velocity = weather_stations[location]['Wind speed']
    #direction
    d = weather_stations[location]['Wind direction']
    #precipitation
    p = weather_stations[location]['Precipitation']
    device = weather_stations[location]['Device']
    print(f'The weather in {location}:')
    print(f'The wind speed is {velocity} m/s in the {d} direction and the precipitation is {p} mm.')
    print(f'The measurement was done using the {device} weather station. \n')