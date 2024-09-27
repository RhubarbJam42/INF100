import csv

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")
    species = {}

    for i in range(2):
        next(akvareader)

    for row in akvareader:
        if row[12] in species:
            species[row[12]] += 1
            continue
        species[row[12]] = 1

    species_list = sorted(species.items(), key=lambda x: x[0])

    for fish, count in species_list:
        print(f'{fish}: {count}')
