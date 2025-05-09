from billboard import Billboard
from spotify import Spotify

# Welcome messages
print("Welcome to the TOP 100 Billboard songs finder")
date = input("What date of songs would you like to find?\nType the date in this format YYYY-MM-DD: ")
playlist_name = input("What name would you like to give this new playlist? ")
print('Excellent, your playlist would be created shortly...')

# Initializing classes
billboard = Billboard()
spotify = Spotify()

# Getting a list of songs from billboard
song_names = billboard.get_songs(date)
print("\nGotten a list of songs from Billboard...\n")

# Getting the URIs of the song list
song_uris = spotify.search_songs(song_names)
if song_uris != "error":

    # Create a playlist and add the songs to it
    print("\nCreating playlist with available songs")
    spotify.create_playlist(playlist_name, song_uris)

    print(f"\nPlaylist '{playlist_name}' created successfully with {len(song_uris)} songs.")
    print("Enjoy the party!!!")
