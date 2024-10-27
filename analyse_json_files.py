import json
from datetime import datetime as dt

file = "recently_played.json"

def get_data(d):
    list_data = []

    track = d["track"]
    # "https://api.spotify.com/v1/tracks/"

    # Interesting data
    track_id = track["id"]
    list_data.append(track_id)
    track_name = track["name"]
    list_data.append(track_name)

    album = track["album"]
    # https://api.spotify.com/v1/albums/

    # Interesting data
    album_name = album["name"]
    list_data.append(album_name)
    album_id = album["id"]
    list_data.append(album_id)
    release_date = album["release_date"]
    list_data.append(release_date)

    # Interesting data
    artistes = track["artists"]
    # print(len(artistes))
    if len(artistes) == 1:
            for artiste in artistes:
                list_data.append(artiste["name"])
                list_data.append(artiste["id"])
                list_data.append("")
    else:
        artistes_secondaires = []
        for i, artiste in enumerate(artistes):
            # https://api.spotify.com/v1/artists/

            if i == 0:
                list_data.append(artiste["name"])
                list_data.append(artiste["id"])
            else:
                print("There is a secundary artist")
                artiste_name = artiste["name"]
                artistes_secondaires.append(artiste_name)
                artiste_id = artiste["id"]
                artistes_secondaires.append(artiste_id)
                # print(artistes_du_morceau)
        list_data.append(artistes_secondaires)

    # Data on myself
    played_at = d["played_at"]
    list_data.append(played_at)
    return list_data

def open_file(file):
    read_file = open(file, mode="r", encoding="utf-8")
    loaded_file = json.load(read_file)

    for item in loaded_file["items"]:
        track_data = get_data(item)
        print(track_data)

    after_date = str({loaded_file["cursors"]["after"]})[2:-2]
    before_date = str({loaded_file["cursors"]["before"]})[2:-2]

    print(f"after = {dt.fromtimestamp(int(after_date)/1000).strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"before = {dt.fromtimestamp(int(before_date)/1000).strftime('%Y-%m-%d %H:%M:%S')}")

open_file(file)