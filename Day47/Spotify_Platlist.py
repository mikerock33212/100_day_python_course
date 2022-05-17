from BillBoardPlaylist import title_of_song, all_singers, Date
import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='playlist-modify-private',
                                               redirect_uri='http://example.com',
                                               client_id='d98818c2f91b4eef8eb4ff4aef60f5f0',
                                               client_secret='a689068f14d04123afef8f817bf2eaa7',
                                               show_dialog=True,
                                               cache_path='token.txt'))

userid = sp.current_user()['id']
song_uri = []
for song in title_of_song:
    result = sp.search(f"track:{song} year:{2022}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri']
        song_uri.append(uri)
    except IndexError:
        print(f'{song} does not exist in spotify, skipped.')

playlist_name = f'BillBoard_Top_100_{Date}'

my_playlist = sp.user_playlist_create(user=userid, name=playlist_name, public=False, collaborative=False)

# track_id = []
# for track in title_of_song:
#     if sp.search(q=track):
#         track_id.append()

sp.playlist_add_items(playlist_id=my_playlist['id'], items=song_uri)

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id='d98818c2f91b4eef8eb4ff4aef60f5f0',
#                                                            client_secret='a689068f14d04123afef8f817bf2eaa7'))
#
# results = sp.search(q='weezer', limit=20)
#
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])