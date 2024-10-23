import json

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

    artiste = track["artists"]
    # https://api.spotify.com/v1/artists/

    # Interesting data
    artiste_name = artiste["name"]
    artiste_id = artiste["id"]


    # Data on myself
    played_at = item["played_at"]
    print(played_at.type())