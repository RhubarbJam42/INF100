#pigify funksjon: Oversetter engelsk til "pig latin"
from copy import copy
def pigify(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    pig_word = ''
    #dersom ordet starter med vokal
    if word[0] in vowels:
        pig_word = copy(word) + 'way'
    #dersom ordet ikke starter med vokal
    else:
        pig_word = list(word)[first_vowel_index(word):] + list(word)[:first_vowel_index(word)]
        pig_word += 'ay'
    return ''.join(pig_word)


def first_vowel_index(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for index, letter in enumerate(word):
        if letter in vowels:
            return index
    return 0


def pigify_sentence(sentence):
    pig_sentence = []
    sentence_list = sentence.split()
    for word in sentence_list:
        pig_sentence.append(pigify(word))
    return ' '.join(pig_sentence)



#test
#print(pigify('oolong'))
#print(pigify('floor'))
#print(pigify_sentence('alice was beginning to get very tired'))