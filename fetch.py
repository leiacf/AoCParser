import urllib.request as url
import json

def get():

    with open(sec, "r") as file:
        secrets = file.read()
        secrets = secrets.replace("\n", " ")
        split = secrets.split(" ")
        board = split[3]
        file.close()

    brd = f"input/{board}.json"

    with open(brd, "r") as file:
        data = json.load(file)

    return data

# Setup

sec = "secrets/secrets.txt"

with open(sec, "r") as file:
    secrets = file.read()
    secrets = secrets.replace("\n", " ")
    split = secrets.split(" ")
    cookie = split[1]
    board = split[3]
    file.close()

path = f"https://adventofcode.com/2023/leaderboard/private/view/{board}.json"
req = url.Request(path, headers={'User-Agent': 'Mozilla/5.0', 'cookie':"session="+cookie})

raw = url.urlopen(req)
data = json.loads(raw.read())

with open (f"input/{board}.json", "w") as file:
    file.write(json.dumps(data, indent=4))
    file.close()

if __name__ == "__main__":
    pass
