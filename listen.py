import spotipy
from time import sleep
from os import system
from pyautogui import typewrite, hotkey, press
path = input("Enter path to downloads folder: ")
print("format: C:\\Users\julius_ist_krass\\folder")
logo = """
                                                                                                                     
bbbbbbbb                                                                                                             
b::::::b                                                 JJJJJJJJJJJ                lllllll   iiii                   
b::::::b              online                             J:::::::::J                l:::::l  i::::i                  
b::::::b                                                 J:::::::::J                l:::::l   iiii                   
 b:::::b                                                 JJ:::::::JJ                l:::::l                          
 b:::::bbbbbbbbb yyyyyyy           yyyyyyy                 J:::::Juuuuuu    uuuuuu   l::::l iiiiiii    ooooooooooo   
 b::::::::::::::bby:::::y         y:::::y                  J:::::Ju::::u    u::::u   l::::l i:::::i  oo:::::::::::oo 
 b::::::::::::::::by:::::y       y:::::y                   J:::::Ju::::u    u::::u   l::::l  i::::i o:::::::::::::::o
 b:::::bbbbb:::::::by:::::y     y:::::y                    J:::::ju::::u    u::::u   l::::l  i::::i o:::::ooooo:::::o
 b:::::b    b::::::b y:::::y   y:::::y                     J:::::Ju::::u    u::::u   l::::l  i::::i o::::o     o::::o
 b:::::b     b:::::b  y:::::y y:::::y          JJJJJJJ     J:::::Ju::::u    u::::u   l::::l  i::::i o::::o     o::::o
 b:::::b     b:::::b   y:::::y:::::y           J:::::J     J:::::Ju::::u    u::::u   l::::l  i::::i o::::o     o::::o
 b:::::b     b:::::b    y:::::::::y            J::::::J   J::::::Ju:::::uuuu:::::u   l::::l  i::::i o::::o     o::::o
 b:::::bbbbbb::::::b     y:::::::y             J:::::::JJJ:::::::Ju:::::::::::::::uul::::::li::::::io:::::ooooo:::::o
 b::::::::::::::::b       y:::::y               JJ:::::::::::::JJ  u:::::::::::::::ul::::::li::::::io:::::::::::::::o
 b:::::::::::::::b       y:::::y                  JJ:::::::::JJ     uu::::::::uu:::ul::::::li::::::i oo:::::::::::oo 
 bbbbbbbbbbbbbbbb       y:::::y                     JJJJJJJJJ         uuuuuuuu  uuuulllllllliiiiiiii   ooooooooooo   
                       y:::::y                                                                                       
                      y:::::y                                                                                        
                     y:::::y                                                                                         
                    y:::::y                          www.grossero.de/julius.de                                                           
                   yyyyyyy                                                                                           
                                                                                                                     
                                                                                                                     
"""
print(logo)
sleep(1)
system("start")
sleep(0.5)
typewrite(f"cd {path}")
sleep(0.2)
press("enter")
sleep(0.2)

CLIENT_ID = "8ab9fb00fd3c413bbf082c0a0b4968ab"
CLIENT_SECRET = "3092457cef4249e1ad5fbcd84eda2a1c"
playlist_link = "https://open.spotify.com/playlist/3fC9GVIb5eXnbS2DVzDFDh?si=5682f6c175194108"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
# PLAYLIST_ID = "3fC9GVIb5eXnbS2DVzDFDh?si=5682f6c175194108"
client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
def download_song(url):
    sleep(0.5)
    typewrite(f"spotdl download {url}")
    press("enter")
    sleep(0.5)
last_time = []
total_tracks = sp.playlist(playlist_URI)["tracks"]["total"]
offset = max(0, total_tracks - 10)
tracks = sp.playlist_items(playlist_URI, offset=offset)["items"]
for track in tracks:
    last_time.append(track["track"]["external_urls"]["spotify"])
this_time = last_time
print(logo)
while True:
    sleep(5)
    total_tracks = sp.playlist(playlist_URI)["tracks"]["total"]
    offset = max(0, total_tracks - 10)
    tracks = sp.playlist_items(playlist_URI, offset=offset)["items"]
    last_time = this_time
    this_time = []
    for track in tracks:
        this_time.append(track["track"]["external_urls"]["spotify"])
    if not all(x == y for x, y in zip(last_time, this_time)):
        for song in this_time:
            if song not in last_time:
                download_song(song)