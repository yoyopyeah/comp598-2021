import json, sys
import pandas as pd
import random

# python3 extract_to_tsv.py -o <out_file> <json_file> <num_posts_to_output>

def load_row(data, line):
    json_obj = json.loads(line)
    name = json_obj['data']['name']
    title = json_obj['data']['title']
    data.append(["{}".format(name), "{}".format(title), ""])


def main():
    outf = sys.argv[2]
    jsonf = open(sys.argv[3], "r")
    post_num = int(sys.argv[4])

    data = []
    i = 0

    if post_num <= 100:
        random_list = random.sample(range(0,99), post_num)
        for line in jsonf:
            if i in random_list:
                load_row(data, line)
            i = i+1 
    else:
        for line in jsonf:
            load_row(data, line)

    df = pd.DataFrame(data, columns=['Name', 'title', 'coding'])
    df.to_csv(outf, sep = '\t', index=False, encoding='utf-8')

    jsonf.close()



if __name__ == "__main__":
    main()