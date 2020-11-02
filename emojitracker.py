# Emojitracker API script

import requests as re
import os
import json
import time

url = "https://api.emojitracker.com/v1/rankings"

def get_rankings():
    res = re.get(url)
    return res
    
def print_to_file():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    with open('rankings_' + timestr + '.txt', 'a') as outfile:
        outfile.write(json.dumps(get_rankings().json(), indent=4, sort_keys=True))
    with open('headers_' + timestr + '.txt', 'a') as outfile:
        outfile.write(str(get_rankings().headers))

def main():
    while True:
        data = get_rankings()
        print_to_file()
        time.sleep(120)


if __name__ == "__main__":
    main()
