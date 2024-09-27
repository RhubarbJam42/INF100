#funksjon som skriver en csv fil fra en annen fil
import csv

rows = [
      ["Come Together", 4, 20, "Lennon/McCartney"],
      ["Something", 3, 3, "Harrison"],
      ["Maxwell's Silver Hammer", 3, 27, "Lennon/McCartney"],
      ["Oh! Darling", 3, 26, "Lennon/McCartney"],
      ["Octopus's Garden", 2, 51, "Starr"],
      ["I want you", 7, 47, "Lennon/McCartney"],
  ]


def write_to_csv(csv_file: str, rows_list: list):
    with open(csv_file, 'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile, delimiter=',')
        for row in rows_list:
            file_writer.writerow(row)
    csvfile.close()
    return None


#write_to_csv('Abbey_Road.csv', rows)
