import json
import requests
import argparse

def main():
    # argparse set up
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--subreddit')
    parser.add_argument('-o', '--output-file')
    args = parser.parse_args()

    subreddit = args.subreddit
    outfile = args.output_file

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

    # retrieve data
    with open (outfile, "w") as f:
        retrieve_data(subreddit, headers, f)

def retrieve_data(subredit, headers, out_file):
    params = {'limit' : 100}
    url = "https://oauth.reddit.com/r/{}/new".format(subredit)
    res = requests.get(url, headers=headers, params=params)
    for i in range(100):
        out_file.write(json.dumps(res.json()['data']['children'][i]))
        out_file.write("\n")


if __name__ == "__main__":
    main()