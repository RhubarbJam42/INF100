#spør om menneskeår og konverterer til hundeår
#De første 2 årene tilsvarer 10.5 hundeår og etter er 1 år 4 hundeår

humanAge = float(input('Angi menneskeår: '))
#for en hund som er opp til og med 2 år gammel: 2 år = 21.0
puppyAge = 10.5
if humanAge <= 2:
    dogAge = puppyAge * humanAge
    print('Dette tilsvarer', dogAge, 'hundeår.')
#for en hund som er eldre enn 2 år gammel
elif humanAge > 2:
    dogAge = 2 * puppyAge + (humanAge - 2) * 4
    print('Dette tilsvarer', dogAge, 'hundeår.')