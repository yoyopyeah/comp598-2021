import json
import argparse
from datetime import datetime
from pytz import timezone
import dateutil.parser


# handles invalid json
def validate_json(x):
    try:
        line = json.loads(x)
        return True
    except Exception:
        # print("json")
        return False

# handles "title"
def validate_title(x):
    line = json.loads(x)
    if "title_text" in line:
        line['title'] = line.pop('title_text')
    elif not "title" in line:
        # print("title")
        return False
    return True

# handles time zone conversion (UTC)
def validate_time(x):
    line = json.loads(x)
    try:
        iso = dateutil.parser.isoparse(line["createdAt"])
    except Exception:
        # print("time")
        return False
    iso = iso.astimezone(timezone('UTC'))
    line["createdAt"] = iso.strftime("%Y-%m-%dT%H:%M:%S%z")
    return True

# handles "author"   
def validate_author(x):
    line = json.loads(x)
    if (not line['author']) or (line['author'] == "N/A"):
        # print("author")
        return False
    return True

# handles "total_count"
def validate_count(x):
    line = json.loads(x)
    if "total_count" in line:
        try:
            int(line["total_count"])
            return True
        except Exception:
            # print("count")
            return False

# handles "tags"
def validate_tags(x):
    line = json.loads(x)
    if "tags" in line:
        line["tags"] = [word for line in line["tags"] for word in line.split()]
    return line["tags"]
    # return json.dumps(line)

def main():
    # set up arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input')
    parser.add_argument('-o', '--output')

    args = parser.parse_args()

    infile = open(args.input, "r")
    outfile = open(args.output, "w")

    #read file & parse by line
    for line in infile:
        if not validate_json(line): continue

        if not validate_title(line): continue

        if not validate_time(line): continue
        
        if not validate_author(line): continue
        
        if not validate_count(line): continue

        line = validate_tags(line)

        # print("success")
        # outfile.write(json.dumps(line) + '\n')
        outfile.write(line + '\n')


    infile.close()
    outfile.close()

if __name__ == "__main__":
    main()