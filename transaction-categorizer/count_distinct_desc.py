with open("2021_merged.csv") as file:
    vendors = {}

    for line in file:
        cols = line.split(",")
        if cols[1] in vendors:
            vendors[cols[1]] += 1
        else:
            vendors[cols[1]] = 1

    #    print(len(vendors.keys()))

    for entry in vendors.items():
        print(entry[0])
