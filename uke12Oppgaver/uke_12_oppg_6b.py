import csv

lats = []
lons = []
species = []

with open("Akvakulturregisteret.csv", newline="", encoding="iso-8859-1") as csvfile:
    akvareader = csv.reader(csvfile, delimiter=";")
    for row in akvareader:
        try:
            lat = float(row[-2])  # latitude is second last
            lon = float(row[-1])  # longitude is last
            fishSpecies = row[12]
        except ValueError:
            continue
        lats.append(lat)
        lons.append(lon)
        species.append(fishSpecies)

try:
    import matplotlib.pyplot as plt
    for fish in range(len(lons)):
        if species[fish] == 'Laks':
            plt.plot(lons[fish], lats[fish], '+r')

    plt.show()
    plt.savefig('uke_12_oppg_6b.png')
except (ImportError, ModuleNotFoundError) as e:
    print(f"Import of matplotlib failed: {e}")
    print(f"We have {len(lats)} latitudes and {len(lons)} longitudes")
