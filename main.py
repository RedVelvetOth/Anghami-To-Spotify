from bs4 import BeautifulSoup

# Getting the HTML FILE

html = open("PATH_FOR_THE_HTML_FILE","r", encoding="utf8")

# Parsing the html file using soup

playlist = BeautifulSoup(html,'html.parser')

# Getting The Titles Of the songs

titles = ["".join(line.strip() for line in ttl.get_text().replace('/n','').splitlines()) for ttl in playlist("div", class_ = "cell cell-title")]

# Getting the Artits Of the Songs

artists = ["".join(line.strip() for line in art.get_text().replace('/n','').splitlines()) for art in playlist("div",class_ = "cell cell-artist")]


import base64

from requests import post,get
import json

# Getting the Access Token

def get_token():
    auth_string = f"{'CLIENT_ID'}:{'CLIENT_SECRET'}"
    auth_byte = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_byte),"utf-8") # The Spotify-API requires that basic token is in a 64 base

    # Creating the header and data requiered for the post 

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/x-www-form-urlencoded",
    }


    data = {"code" : "CODE_GENERATED",
            "redirect_uri" :"http://127.0.0.1:5000/redirect",
            "grant_type" : "authorization_code",} # We specify the type so as to get a token that will allow us to create playlists, add titles and so on.

    result = post(url,headers=headers,data=data)
    return json.loads(result.content)["access_token"]

# Create the Header Required For All future Operations

def get_auth_header(token):
    return {"Authorization": f"Bearer {token}",
        "Content-Type": "application/json"}


# Get The Id Of The Song 

def search_for_song(token,artist_name,track_title):
    url = "https://api.spotify.com/v1/search"

    headers = get_auth_header(token)

    query = f"?q={track_title,artist_name}&type=track"

    query_url = url + query

    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    return json_result[0]["uri"] # Only displays the ID of the track


# Create The Playlist in which we'll add our titles

def create_playlist(token):
    user_id = 'USER_ID'
    url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    headers = get_auth_header(token)

    request_body = json.dumps({
          "name": "Meine Edelsteine", # Name of the playlist 
          "description": "My Gems", # The description of the playlist
          "public": False
        })

    result = post(url,headers=headers,data=request_body)
    return json.loads(result.content)



# Add a Title To Specified Playlist

def add_items(token,uris,id):
    url = f"https://api.spotify.com/v1/playlists/{id}/tracks" # We have to specify the id of the playlist 

    headers = get_auth_header(token)

    request_body = json.dumps({
          "uris": [uris]
        })

    result = post(url,headers=headers,data=request_body)

    print(result)
    

# Does The Rest Of The Magic

def add_all_tracks():
    token = get_token()

    id_ = create_playlist(token)["id"]

    for i in range(0,len(artists) - 1):
        artist,title = artists[i],titles[i]
        uris = search_for_song(token,artist,title)
        add_items(token,uris,id_)


add_all_tracks()




