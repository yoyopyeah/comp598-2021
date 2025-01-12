import pandas as pd
import argparse, json
from csv import reader

def main():
    # argparse set up
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--script_input', required=True)
    parser.add_argument('-o', '--network', required=True)
    args = parser.parse_args()

    # parse dialog & build data
    data = {}
    df = pd.read_csv(args.script_input)
    most_freq = get_most_freq(df)

    prev = ""
    title = df.iloc[0]["title"]

    for pony in most_freq:
        data[pony] = {}

    with open(args.script_input, 'r') as f
        freader = reader(f)
        next(freader) #skip header
        first = next(freader)

        prev_char = ""
        prev_title = ""

        cur_char = first[2].lower()
        cur_title = first[0]

    for row in df.itertuples():
        # print("----------")
        cur = row.pony.lower()
        flag = False

        # check general terms not in cur
        for word in ["others", "ponies", "and", "all"]:
            if word in cur.split(): 
                prev = ""
                flag = True
                break
        if flag: continue

        # check if cur is 101 most freq characters
        if cur not in most_freq:
            prev = ""
            continue
            
        # check if prev == ""
        if prev == "":
            prev = cur
            continue

        # check interactions stay in one episode
        if title != row.title: 
            title = row.title
            prev = cur
            continue

        # check if there exists prev != cur
        if prev == cur: continue
        
        # add interaction between prev and cur to network
        if cur not in data[prev]:
            data[prev][cur] = 0
        if prev not in data[cur]:
            data[cur][prev] = 0

        data[prev][cur] += 1
        data[cur][prev] += 1

        # update prev
        prev = cur

    # --- end for loop

    with open(args.network, 'w') as f:
        json.dump(data, f, indent=4)
    


def get_most_freq(df):
    # return dict contain 101 most frequent characters
    # var = df["pony"].value_count().index.tolist()
    result = {}
    for row in df.itertuples():
        flag = False
        pony = row.pony

        if not pony.lower() in result:
            for word in ["others", "ponies", "and", "all"]:
                if word in pony.lower().split():
                    flag = True
                    break
            if flag: continue
    
            result[pony.lower()] =  df["pony"].value_counts()[pony]
            
    result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))
    if len(result) < 101:
        return list(result)
    else return list(result)[:101]


if __name__ == "__main__":
    main()