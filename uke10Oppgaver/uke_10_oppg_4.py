#første bokstav av siste ord i hver linje
def first_letter_last_word(filename):
    with open(filename, 'r', encoding='utf8') as file:
        lines = [line.split() for line in file]
        file.close()
    last_word = [item[len(item)-1] for item in lines]
    first_let = ''
    for word in last_word:
        first_let += word[0]
    return first_let

#test
#print(first_letter_lastword('askeladden.txt'))