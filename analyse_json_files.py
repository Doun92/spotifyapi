import json
from datetime import datetime as dt

file = "recently_played.json"

read_file = open(file, mode="r", encoding="utf-8")
data = json.load(read_file)

# print(data["items"])

for item in data["items"]:
    track = item["track"]
    # "https://api.spotify.com/v1/tracks/"

    # Interesting data
    track_name = track["name"]
    track_id = track["id"]

    album = track["album"]
    # https://api.spotify.com/v1/albums/

    # Interesting data
    album_name = album["name"]
    release_date = album["release_date"]
    album_id = album["id"]

    artistes = track["artists"]
    artistes_du_morceau = []
    for artiste in artistes:
        # print(artiste)
        # https://api.spotify.com/v1/artists/

        # Interesting data
        artiste_name = artiste["name"]
        artistes_du_morceau.append(artiste_name)
        artiste_id = artiste["id"]
        artistes_du_morceau.append(artiste_id)
    # print(artistes_du_morceau)

    # Data on myself
    played_at = item["played_at"]
    # print(played_at.type())

after_date = str({data["cursors"]["after"]})[2:-2]
before_date = str({data["cursors"]["before"]})[2:-2]

print(f"after = {dt.fromtimestamp(int(after_date)/1000).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"before = {dt.fromtimestamp(int(before_date)/1000).strftime('%Y-%m-%d %H:%M:%S')}")
