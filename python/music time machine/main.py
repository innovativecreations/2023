# import requests as r
# from bs4 import BeautifulSoup
#
# re = r.get(url="https://www.billboard.com/charts/hot-100/2000-08-12/")
#
# soup = BeautifulSoup(re.text, "html.parser")
# print(soup.find_all(name="h3", id="title-of-a-story", class_='c-title'))
# songs = [song.getText() for song in soup.find_all(name="h3", id="title-of-a-story")]
#
# print(songs)
#
######################## Not woking ##########################



import spotipy
from spotipy.oauth2 import SpotifyOAuth


scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])