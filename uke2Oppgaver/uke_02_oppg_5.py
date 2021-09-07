# Leser inn navn, adresse, postnummer og poststed, og så bestemmer lengste rad
name = input('Hva er ditt navn? ')
address = input('Hva er din adresse? ')
postalCode = input('Hva er ditt postnummer og poststed? ')
lengthName = len(name)
lengthAddress = len(address)
lengthPostalCode = len(postalCode)
longestInput = max(lengthName, lengthPostalCode, lengthAddress)
print(longestInput)
