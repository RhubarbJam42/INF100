# Leser inn navn, adresse, postnummer og poststed for så å bestemme kun første lengste rad å printe ut
name = input('Hva er ditt navn? ')
address = input('Hva er din adresse? ')
postalCode = input('Hva er ditt postnummer og poststed? ')
lengthName = len(name)
lengthAddress = len(address)
lengthPostalCode = len(postalCode)
longestInput = max(lengthName, lengthPostalCode, lengthAddress)

if longestInput == lengthName:
    print(name)
elif longestInput == lengthAddress:
    print(address)
elif longestInput == lengthPostalCode:
    print(postalCode)
