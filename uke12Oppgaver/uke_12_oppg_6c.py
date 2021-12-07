import csv

lats = []
lons = []
waterType = []

with open('Akvakulturregisteret.csv', newline='', encoding='iso-8859-1') as csvfile:
    akvareader = csv.reader(csvfile, delimiter=';')
    for row in akvareader:
        try:
            lat = float(row[-2]) # latitude is second last
            lon = float(row[-1]) # longitude is last
            water = row[20] #water type is the 20th
        except ValueError:
            continue
        lats.append(lat)
        lons.append(lon)
        waterType.append(water)


try:
    import matplotlib.pyplot as plt
    for i in range(len(lons)):
        if waterType[i] == 'SALTVANN':
            plt.plot(lons[i], lats[i], '+r')
        else:
            plt.plot(lons[i], lats[i], '+b')

    plt.show()
except (ImportError, ModuleNotFoundError) as e:
    print(f'Import of matplotlib failed: {e}')
    print(f'We have {len(lats)} latitudes and {len(lons)} longitudes')
