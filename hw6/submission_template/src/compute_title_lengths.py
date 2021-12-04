# accept an input file containing one JSON dict per line (corresponding to a subreddit post) 
# and output the average post title length – 
# in essence, it should accept one of the sample.json files produced by the collect.py script. 
# The input JSON dict should respect *exactly* the format returned by reddit’s API. 
# The script is called like: python3 compute_title_lengths.py <input_file>.

import json
import sys

def main():
    input_file = open(sys.argv[1], "r")
    total_len = 0
    for line in input_file:
        json_obj = json.loads(line)
        total_len = total_len + len(json_obj["data"]["title"])
    print(round(total_len / 1000, 2))


if __name__ == "__main__":
    main()