#funksjon som beregner trykk i havet på en gitt dybde

def hyd_pres(p, g, z):
    return p * g * z * 1e-4
#p = vanndensiteten, g = tyngdekraftens akselerasjon z = dybde til partikkel
#p * g * z = verdi med enhet Pa (pascal). Ganget med 1e-4 gir enhet i dbar (decibar)

#print(hyd_pres(1025, 10, 100)) = 102.5 (dbar)