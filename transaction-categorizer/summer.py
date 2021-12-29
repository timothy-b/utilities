import csv
import re

with open("2021_merged.csv") as file:
    vendors = {}

    line_number = 0
    csvreader = csv.reader(file)
    sum = 0
    for row in csvreader:
        if re.match(".*ebay", row[1], flags=re.IGNORECASE):
            print(row)
            sum += float(row[2].replace(",", ""))

    print(sum)
