#for-loop som skriver ut alle bokstaver til høyteknologisenteret på hver sin linje
buildingName = 'høyteknologisenteret'
charactersBuilding = int(len(buildingName))
for letters in range(0, charactersBuilding):
    print(buildingName[letters])