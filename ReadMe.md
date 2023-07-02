
# Anghami To Spotify Migrater

This Python script allows you to migrate your playlists from Anghami to Spotify.

This script utilizes the Spotify API (unfortunately Anghami's is not publicly available but there's a way around it)

## Prerequisites

Before running this script, ensure the following is installed on your machine:

    1. Pyhton 3.x
    2. pip

Additionally, make sure to install the required dependencies.

```python
    pip install beautifulsoup4

    pip install requests

    pip install spotipy

    pip install flask
```

# Getting Started

1. Navigate to the playlist ( or downloads and likes) you want to duplicate on Anghami's web player. Make sure all the songs are loaded and viewable by scrolling to the bottom of the playlist.

2. To save a web page it's `ctrl + s`.

3. Log in or register for a new account at Spotify for Developers - https://developer.spotify.com/dashboard/.

4. Once logged in, go to the dashboard and create a new app. 

5. After creating the app, copy the **CLIENT ID** and **CLIENT SECRET** values. You may need to click on "Show Client Secret" to reveal it.

6. Click on "Edit Settings" for your app and set the "Redirect URI" to http://127.0.0.1:5000/redirect. After authentication, spotify will reroute users to this website.

7. Run the `authentif.py`, where the CLIENT_ID and CLIENT_SECRET are those copied earlier. 

8. After opening the http://127.0.0.1:5000/redirect you'll a code will be displayed, copy its value.

9. Navigate to the `get_token()` function  in `main.py` and replace the code value in the data dictionary with the one copied.

10. Voila! Your playlists are getting migrated.


# Note

Note this is not a 100% accuarte script. There are minute instances where it may upload the wrong version of the song or another song instead of the one in the original playlist.