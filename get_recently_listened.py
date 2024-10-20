import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import json

# Load secret .env file
load_dotenv()

# Define Crendetials
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')
base_address = "https://api.spotify.com."

def login(c_id,c_secret,r_uri):
    # Define the scope you need (permissions)
    scope = 'user-library-read user-read-playback-state user-modify-playback-state user-top-read user-read-recently-played'

    # Create a SpotifyOAuth object for authentication
    sp_oauth = SpotifyOAuth(
        client_id=c_id,
        client_secret=c_secret,
        redirect_uri=r_uri,
        scope=scope
    )

    # Create a Spotify client using the authenticated credentials
    sp = spotipy.Spotify(auth_manager=sp_oauth)

    # Test the connection by getting the current user's profile information
    user_profile = sp.current_user()
    print(f"Connected to Spotify as: {user_profile['display_name']}")

    return sp

sp = login(client_id,client_secret,redirect_uri)

recently_played = sp.current_user_recently_played()
# Serializing json
json_object = json.dumps(recently_played, indent=4)
# Writing to sample.json
with open("recently_played.json", "w") as outfile:
    outfile.write(json_object)