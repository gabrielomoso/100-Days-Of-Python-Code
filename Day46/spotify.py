import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.exceptions import SpotifyException

# Set up Spotipy with your client credentials and redirect URI
CLIENT_ID = ""
CLIENT_SECRET = ""
REDIRECT_URI = 'http://localhost:9999/callback'

# Initialize Spotipy client with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="playlist-modify-public",
                                               cache_path="token.txt"))


class Spotify:
    # Define a function to search for song names
    def search_songs(self, song_names):
        """This function searches for a list of songs using its song names and returns its URIs"""
        song_uris = []
        for song_name in song_names:
            # Search for the song

            # Exception handler incase user not added to the dashboard
            try:
                results = sp.search(q=song_name, type='track', limit=1)

                # Extract relevant information from the search results
                if results['tracks']['items']:
                    track = results['tracks']['items'][0]
                    song_uris.append(track['uri'])
                else:
                    print(f"Could not find '{song_name}' on Spotify...")
            except SpotifyException as e:
                if e.http_status == 403:
                    print("\nHello there... This should be your first time using this program")
                    print('Please send a DM to my twitter(X) account "@GabzCode" with your name and email')
                    print("I will need to add you to my spotify Dashboard so you can use this program")
                    print("Its a spotify thing😉, Only few slots remaining")
                    return "error"
                else:
                    print("This is odd, An unexpected error.")
                    print(
                        "Kindly send the error message below to gabrielomoso@gmail.com and I will try and fix the issue")
                    raise

        return song_uris

    # Define a function to create a playlist and add songs to it
    def create_playlist(self, playlist_name, song_uris):
        """This function creates a playlist using a list of URIs and adds to a spotify account"""
        user_id = sp.me()['id']
        playlist = sp.user_playlist_create(user_id, playlist_name, public=True)
        playlist_id = playlist['id']
        sp.playlist_add_items(playlist_id, song_uris)
