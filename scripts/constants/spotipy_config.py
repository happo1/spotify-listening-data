import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

if not CLIENT_ID or not CLIENT_SECRET:
    raise ValueError("Missing environment variables")

def get_spotify_client():
    
    '''
    Returns a spotipy client instance authenticated with the provided
    CLIENT_ID and CLIENT_SECRET.
    '''
    
    auth_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET
    )

    return spotipy.Spotify(
        auth_manager=auth_manager,
        requests_timeout=10,
        retries=5,
        status_retries=5,
        status_forcelist=[429, 500, 502, 503, 504]
    )