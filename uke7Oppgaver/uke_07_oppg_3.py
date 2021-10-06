#funksjon som justerer en verdi inne i en tuple
from copy import deepcopy


def adjust_daily_temps(daily_temperatures):
    to_adjust = list(deepcopy(daily_temperatures))
    to_adjust[3] = ('torsdag', 12.0)
    return tuple(to_adjust)

#test
'''print(adjust_daily_temps((
  ("mandag", 16.0),
  ("tirsdag", 13.0),
  ("onsdag", 14.0),
  ("torsdag", 13.0),
  ("fredag", 15.0),
  ("lørdag", 13.0),
)))'''