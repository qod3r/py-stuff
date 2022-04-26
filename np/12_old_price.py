import csv

with open("old_price.csv", 'r', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        if int(row['Old price']) > int(row['New price']):
            print(row['Name'])
            