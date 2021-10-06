#funksjon som bytter ut en verdi i en tuple
def swap_tuple(cat):
    #multiple assignment trick. Variablene blir assigned til indexene i den rekkefølgen
    name, personality, food = cat
    food = 'salmon'
    return (name, personality, food)

#test
#print(swap_tuple(("Princess Sparkle", "aloof", "tuna")))