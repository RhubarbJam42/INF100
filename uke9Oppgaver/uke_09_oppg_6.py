# sjekker bøker hos en bokhandel med en dictionary

inStorage = {
    "Ancillary Justice": 1_046,
    "The Use of Weapons": 372,
    "1984": 5_332,
    "The Three-Body Problem": 523,
    "A Fisherman of the Inland Sea": 728,
}

while True:
    title = input('Tittel: ')
    if title == '':
        print('Ha det!')
        break
    elif inStorage.get(title, 0) == 0:
        inStorage.setdefault(str(title), 10)
        print('Vi har', str(inStorage.get(title)), 'av', f'"{title}"\n')
    else:
        print('Vi har', str(inStorage.get(title)), 'av', f'"{title}"\n')