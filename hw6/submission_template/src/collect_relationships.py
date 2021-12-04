import json, bs4, argparse, os, requests

def main():
    # argparse set up
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config-file')
    parser.add_argument('-o', '--output-file')
    args = parser.parse_args()

    # checking and opening config and output files
    config_file = open(args.config_file, )
    config = json.load(config_file)

    outfile = args.output_file
    os.makedirs(os.path.dirname(outfile), exist_ok=True)
    outfile = open(outfile, "w")

    # set up output json
    out_json = {}

    # set up cache directory
    cache_dir = config["cache_dir"]
    celebs = config["target_people"]

    URL = "https://www.whosdatedwho.com/dating/"

    for celeb in celebs:
        date_list = []
        celeb_file = os.path.join(cache_dir, celeb)

        # if file not cached, create new file
        if not os.path.isfile(celeb_file):
            os.makedirs(os.path.dirname(celeb_file), exist_ok=True)
            page = requests.get("{}{}".format(URL, celeb))
            with open(celeb_file, 'w') as f:
                f.write(page.text)

        # get the soup rolling
        soup = bs4.BeautifulSoup(open(celeb_file, 'r'), 'html.parser')
        grids = soup.find_all('div', 'ff-grid-box')
        for div in grids:
            name = div.get('id').replace('dating-','')
            date_list.append(name)

        # add relationships to out_json
        out_json[celeb] = date_list

    outfile.write(json.dumps(out_json, indent=2))
    config_file.close()
    outfile.close()


if __name__ == "__main__":
    main()