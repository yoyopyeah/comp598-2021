# python3 analyze.py -i <coded_file.tsv> [-o <output_file>]

import argparse, json
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--coded-file')
    parser.add_argument('-o', '--output-file')
    args = parser.parse_args()

    json_obj = {
        "course-related": 0, 
        "food-related": 0, 
        "residence-related": 0, 
        "other": 0
    }

    df = pd.read_csv(args.coded_file, sep='\t')
    for row in df.itertuples():
        if row.coding == 'c':
            json_obj["course-related"] +=  1
        elif row.coding == 'f':
            json_obj["food-related"] +=  1
        elif row.coding == 'r':
            json_obj["residence-related"] +=  1
        elif row.coding == 'o':
            json_obj["other"] +=  1


    if args.output_file is None:
        # print to stdout
        print(json.dumps(json_obj, indent=4))
    else:
        with open(args.output_file, "w") as f:
            json.dump(json_obj, f, indent=4)


if __name__ == "__main__":
    main()