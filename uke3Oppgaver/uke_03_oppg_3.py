# inputter en enhet og bestemmer utifra enhet og verdi hva slags elektromagnetisk stråling disse er

unit = input('Angi enhet: ')
value = float(input('Angi verdi: '))

if unit == 'nm' and value >= 1e9 or unit == 'THz' and value <= 3e-4:
    print('Dette er radiobølger.')
elif unit == 'nm' and 1e9 > value >= 1e6 or unit == 'THz' and 3e-4 < value <= 0.3:
    print('Dette er mikrobølger.')
elif unit == 'nm' and 1e6 > value >= 740 or unit == 'THz' and 0.3 < value <= 405:
    print('Dette er infrarød stråling.')
elif unit == 'nm' and 740 > value >= 380 or unit == 'THz' and 405 < value <= 790:
    print('Dette er synlig lys.')
elif unit == 'nm' and 380 > value >= 10 or unit == 'THz' and 790 < value <= 3e4:
    print('Dette er ultrafiolett lys.')
elif unit == 'nm' and 10 > value >= 0.01 or unit == 'THz' and 3e4 < value <= 3e7:
    print('Dette er røntgenstråling.')
elif unit == 'nm' and 0.01 > value or unit == 'THz' and 3e7 < value:
    print('Dette er gammastråling.')

#for å varsle feil dersom noe er plotta inn feil
else:
    print('error')