import json
import re
import csv

categories = []
category_map = {}

with open("category_mapping.json") as file:
    data = json.load(file)
    print("loaded categories:")
    for category in data["categories"]:
        print(category)
        categories.append(category)

    for mapping in data["mappings"].items():
        category_map[mapping[0]] = mapping[1]

category_column = []

with open("2021_merged.csv") as file:
    vendors = {}

    line_number = 0
    csvreader = csv.reader(file)
    for row in csvreader:
        line_number += 1

        vendor = row[1]

        found_category = False
        for pattern in category_map.keys():
            if re.match(pattern, vendor):
                category_column.append(category_map[pattern])
                found_category = True
                break

        if not found_category:
            new_pattern_accepted = False
            print(f"row {line_number}")
            print("name the category for the following transaction:")
            print(row)
            print(vendor)
            pattern = ""
            category = input()

            while not new_pattern_accepted:
                pattern = input("set the regex for the transaction vendor:")

                if re.match(pattern, vendor):
                    categories.append(pattern)
                    new_pattern_accepted = True
                else:
                    print(
                        "The regex did not match the current vendor. Please try again."
                    )

            category_map[pattern] = category

            file_category_mappings = []
            with open("category_mapping.json", "r") as file:
                file_category_mappings = json.load(file)
            with open("category_mapping.json", "w") as file:
                if category not in file_category_mappings["categories"]:
                    file_category_mappings["categories"].append(category)

                file_category_mappings["categories"].sort()
                file_category_mappings["mappings"][pattern] = category
                json.dump(file_category_mappings, file, indent=2)

            category_column.append(category)

with open("output.txt", "w") as output_file:
    output_file.write("\n".join(category_column))
