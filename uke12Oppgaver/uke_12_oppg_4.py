#funksjon som leser fil og printer ut første kolonne i fil
import csv

def read_first_col(csv_file):
    with open(csv_file, newline='') as csvfile:
        data_reader = csv.reader(csvfile, delimiter=' ')
        for row in data_reader:
            print(row[0])
    return None

read_first_col('2019-06-01_Oslo.csv')