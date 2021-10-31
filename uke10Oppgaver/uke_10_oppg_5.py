#finnes filen?
def first_letter_last_word(filename):
    with open(filename, 'r', encoding='utf8') as file:
        lines = [line.split() for line in file]
        file.close()
    last_word = [item[len(item)-1] for item in lines]
    first_let = ''
    for word in last_word:
        first_let += word[0]
    return first_let


def first_letters(filename):
    try:
        return first_letter_last_word(filename)
    except FileNotFoundError:
        return ''

#test
#print(first_letter('askeladden.txt'))
#print(first_letter('aseladden.txt'))