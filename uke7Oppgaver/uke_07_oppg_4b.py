#reorganiserer data gitt til funksjonen

def data_reorganize(data):
    return tuple(zip(*data))

#test
'''print(data_reorganize((
  ("mandag", 16.0),
  ("tirsdag", 13.0),
  ("onsdag", 14.0),
  ("torsdag", 13.0),
  ("fredag", 15.0),
  ("lørdag", 13.0),
)))'''