import json
import csv

# base structure
base = {
    "count": {
        "twilight sparkle": 0,
        "applejack": 0,
        "rarity": 0,
        "pinkie pie": 0,
        "rainbow dash": 0,
        "fluttershy": 0
    },
    "verbosity": {
        "twilight sparkle": 0,
        "applejack": 0,
        "rarity": 0,
        "pinkie pie": 0,
        "rainbow dash": 0,
        "fluttershy": 0
    } 
}

total = -1

with open ('../data/clean_dialog.csv') as data:
    reader = csv.reader(data, delimiter=',')
    for row in reader:
        total += 1
        for pony in base["count"]:
            if pony in row[2].lower():
                base["count"][pony] += 1
    for pony in base["verbosity"]:
        base["verbosity"][pony] = round(base["count"][pony] / total, 2)

print(total)

# result = json.dumps(base)

# with open ('../output.json', 'w') as outfile:
#     json.dump(base, outfile)
#     print(json.dumps(base, indent=1))

f = open("../output.json", "w")
f.write(json.dumps(base, indent=1))
f.close()

