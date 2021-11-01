import json
import argparse
from datetime import datetime
from pytz import timezone
import dateutil.parser


def main():
    # set up arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    args = parser.parse_args()

    infile = open(args.input, "r")
    outfile = open(args.output, "w")

    i = 1
    #read file & parse by line
    for x in infile:
        print("---------")
        print(f"reached {i}")

        try:
            line = json.loads(x)

        # handles invalid json
        except Exception:
            print("*** exception caught")
            i = i + 1
            continue

        # handles "title"
        if "title_text" in line:
            # rename to "title"
            line['title'] = line.pop('title_text')
        elif not "title" in line:
            # remove posts without "title" nor "title_text"
            print("*** title")
            i = i + 1
            continue

        # handles time zone conversion (UTC)
        try:
            iso = dateutil.parser.isoparse(line["createdAt"])
        except Exception:
            print("*** time format")
            i = i + 1
            continue
        iso = iso.astimezone(timezone('UTC'))
        line["createdAt"] = iso.strftime("%Y-%m-%dT%H:%M:%S%z")
        
        # handles "author"
        if (not line['author']) or (line['author'] == "N/A"):
            print("*** author")
            i = i + 1
            continue

        # handles "total_count"
        if "total_count" in line:
            try:
                int(line["total_count"])
            except Exception:
                print("*** total_count")
                i = i + 1
                continue

        # handles "tags"
        if "tags" in line:
            line["tags"] = [word for line in line["tags"] for word in line.split()]
        
        i = i + 1
        print(">3<")
        outfile.write(json.dumps(line) + '\n')


    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()