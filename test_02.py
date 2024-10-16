import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load secret .env file
load_dotenv()

# Define Crendetials
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
redirect_uri = os.getenv('redirect_uri')

# Define the scope you need (permissions)
scope = 'user-library-read user-read-playback-state user-modify-playback-state'

# Create a SpotifyOAuth object for authentication
sp_oauth = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
)

# Create a Spotify client using the authenticated credentials
sp = spotipy.Spotify(auth_manager=sp_oauth)

# Test the connection by getting the current user's profile information
user_profile = sp.current_user()
print(f"Connected to Spotify as: {user_profile['display_name']}")
