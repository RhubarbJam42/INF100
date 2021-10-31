#Gi navn til filer som beskriver filen utifra data i filen
def rename_from_data(filename):
    with open(filename, 'r', encoding='utf8') as datafile:
        area_date = [next(datafile) for i in range(2)]
        area = area_date[0].strip()
        date = area_date[1].strip()
        renamed_filename = f'{date}_{area}.txt'

        with open(renamed_filename, 'w', encoding='utf8')as new_file:
            for line in datafile:
                new_file.write(line)
    return None


def rename_all(namelist: list):
    for file in namelist:
        rename_from_data(file)
    return None


#rename_all(['qwerty.txt', 'qwghlm.txt'])