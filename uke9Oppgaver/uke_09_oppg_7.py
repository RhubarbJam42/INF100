# funksjon som sammenligner 2 ord og returnerer likeheter, bokstaver unike til første ord og bokstaver unik til
# det andre ordet

def word_comparison(word_one, word_two):
    first_list = list(word_one)
    second_list = list(word_two)

    common_set = {letter for letter in first_list if letter in second_list}
    first_unique = {l for l in first_list if l not in second_list}
    sec_unique = {n for n in second_list if n not in first_list}

    word_compare = {'In common': common_set, 'Unique to first word': first_unique, 'Unique to second word': sec_unique}

    return word_compare

#test
#print(word_comparison('computer', 'science'))
