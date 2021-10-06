#funksjon som tar inn liste med data og returnerer listen med betegnelse av kalibreringstidspunkt
def calibration_readout(wind_velocity):
    for index, velocity in enumerate(wind_velocity):
        if index % 12 == 0:
            wind_velocity[index] = ('Calibration hour', velocity)
    return wind_velocity

#test
#print(calibration_readout([3.0, 3.2, 3.3, 3.2, 3.0, 3.1, 3.5, 5.0, 5.0, 4.9, 4.0, 3.0, 2.9, 2.2]))
