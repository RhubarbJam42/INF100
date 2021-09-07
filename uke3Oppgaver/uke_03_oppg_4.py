# får inn et årstall og gir ut om det er et skuddår eller ikke
# er et skuddår dersom delelig på 4, men år som er delelig på 100 er ikke skuddår og utenom år som er delelig på 400
year = int(input('Angi år: '))
leapYear = False
checkYearDividedByFour = year % 4
checkYearDividedByHundred = year % 100
checkYearDividedByFourHundred = year % 400

if checkYearDividedByFour == 0 and checkYearDividedByHundred != 0:
    leapYear = True
elif checkYearDividedByFour == 0 and checkYearDividedByHundred == 0:
    if checkYearDividedByFourHundred == 0:
        leapYear = True
    else:
        leapYear = False

if leapYear:
    print('Dette er et skuddår.')
else:
    print('Dette er ikke et skuddår.')
