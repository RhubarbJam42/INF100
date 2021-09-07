# Leser inn navn, adresse, postnummer og poststed for så å printe de lengste radene
name = input('Hva er ditt navn? ')
address = input('Hva er din adresse? ')
postalCode = input('Hva er ditt postnummer og poststed? ')
lengthName = len(name)
lengthAddress = len(address)
lengthPostalCode = len(postalCode)
longestInput = max(lengthName, lengthPostalCode, lengthAddress)

if longestInput == lengthName and longestInput == lengthAddress and longestInput == lengthPostalCode:
    print(name)
    print(address)
    print(postalCode)
elif longestInput == lengthName and longestInput == lengthAddress:
    print(name)
    print(address)
elif longestInput == lengthAddress and longestInput == lengthPostalCode:
    print(address)
    print(postalCode)
elif longestInput == lengthPostalCode and longestInput == lengthName:
    print(name)
    print(postalCode)
elif longestInput == lengthName and longestInput != lengthAddress and longestInput != lengthPostalCode:
    print(name)
elif longestInput != lengthName and longestInput == lengthAddress and longestInput != lengthPostalCode:
    print(address)
elif longestInput != lengthName and longestInput != lengthAddress and longestInput == lengthPostalCode:
    print(postalCode)

