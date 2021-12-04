import pandas as pd
import networkx as nx
import pandas as pd
import argparse, json

def main():
    # argparse set up
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--script_input', required=True)
    parser.add_argument('-o', '--network', required=True)
    args = parser.parse_args()

    # parse dialog & build network
    G = nx.Graph()
    df = pd.read_csv(args.script_input)
    most_freq = get_most_freq(df)

    prev = ""
    title = df.iloc[0]["title"]

    for row in df.itertuples():
        # print("----------")
        cur = row.pony.lower()
        flag = False

        # check general terms not in cur
        for word in ["others", "ponies", "and", "all"]:
            if word in cur.split(): 
                prev = ""
                flag = True
                continue
        if flag: continue

        # check if cur is 101 most freq characters
        if not cur in most_freq:
            prev = ""
            continue
            
        # check if prev == ""
        if prev == "":
            prev = cur
            continue

        # check interactions stay in one episode
        if title != row.title: 
            title = row.title
            prev = ""
            continue

        # check if there exists prev != cur
        if prev == cur: continue
        
        # add interaction between prev and cur to network
        if G.has_edge(prev, cur): 
            G[prev][cur]['weight'] += 1
        else: 
            G.add_edge(prev, cur, weight=1)

        # update prev
        prev = cur

    # --- end for loop

    # generate json from network
    json_obj = {}

    for pony1 in most_freq:
        json_obj[pony1] = {}
        for pony2 in most_freq:
            if pony1 == pony2: continue

            if G.has_edge(pony1, pony2):
                json_obj[pony1][pony2] = G[pony1][pony2]['weight']

    with open(args.network, 'w') as f:
        json.dump(json_obj, f, indent=4)
    


def get_most_freq(df):
    # return dict contain 101 most frequent characters
    result = {}
    for row in df.itertuples():
        flag = False
        pony = row.pony

        if pony.lower() not in result:
            for word in ["others", "ponies", "and", "all"]:
                if word in pony.lower().split():
                    flag = True
            if flag: continue
    
            result[pony.lower()] =  df["pony"].value_counts()[pony]
            
            result = dict(sorted(result.items(), key=lambda item: item[1], reverse = True))

    result = list(result)
    return list(result)[:101]


if __name__ == "__main__":
    main()