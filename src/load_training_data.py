import csv

whales = []

with open("../whale-categorization-playground/train.csv", "r") as data:
    reader = csv.reader(data)

    for row in reader:
        whales.append(row)

print(whales[0])
