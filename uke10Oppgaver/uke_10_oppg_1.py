#åpner fil og returnerer alle newlines og whitespace

def open_file(filename):
    with open(filename, 'r', encoding='utf8') as file:
        return str(file.read())


#print(open_file('askeladden.txt'))
