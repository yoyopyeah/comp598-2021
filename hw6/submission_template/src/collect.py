# collecting the data for BOTH of the sampling approaches. 
# It should store the data (as received from Reddit) in files sample1.json and sample2.json (respectively). 
# Reddit's API wraps posts into a key called "children", 
# so sample1.json and sample2.json files must store the contents of the children tag. 

import json
import requests

def main():
    # set ups
    CLIENT_ID = "MaLfE1iN1JT62zk4iyfo2g"
    SECRET_KEY = "6ldK2BCPs6qY169qYtxuh3invtz7Dw"
    auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_KEY)
    data = {
        'grant_type': 'password',
        'username': 'comp598_struggle',
        'password': 'gewuzhizhi'
    }
    headers = {'User-Agent': 'comp598/0.0.1'}
    res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)
    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}
    ###

    # retrieve Sample 1 data
    f = open("sample1.json", "w")
    for subredit in ["funny", "AskReddit", "gaming", "aww", "pics", "Music", "science", "worldnews", "videos", "todayilearned"]:
        retrieve_data(subredit, headers, f)
    f.close()

    # retrieve Sample 2 data
    f = open("sample2.json", "w")
    for subredit in ["AskReddit", "memes", "politics", "nfl", "nba", "wallstreetbets", "teenagers", "PublicFreakout", "leagueoflegends", "unpopularopinion"]:
        retrieve_data(subredit, headers, f)
    f.close()

def retrieve_data(subredit, headers, out_file):
    params = {'limit' : 100}
    url = "https://oauth.reddit.com/r/{}/new".format(subredit)
    res = requests.get(url, headers=headers, params=params)
    for i in range(100):
        out_file.write(json.dumps(res.json()['data']['children'][i]))
        out_file.write("\n")


if __name__ == "__main__":
    main()