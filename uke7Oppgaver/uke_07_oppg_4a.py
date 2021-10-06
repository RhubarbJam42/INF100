#funksjon som tar to tupler og gir 2 verdier i en liste tilbake

def tuple_repack(tuple_one, tuple_two):
    #lager tuplene om til en zip for så å returnere liste med index av listen til zip
    zip_tuple = zip(tuple_one, tuple_two)
    return list(list(zip_tuple)[1])

#test
#print(tuple_repack(("Princess Sparkle", "aloof", "tuna"), ("Mr Cat", "energetic", "cream")))