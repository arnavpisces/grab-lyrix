#Python script to fetch current playing song from spotify and get the lyrics for it in realtime - (later: timestamped lyrics with text highlighting)

import requests, json, lyricsgenius, time
songName=""
artistName=""

def getSongDetails():
  global songName
  global artistName
  genius = lyricsgenius.Genius('ST540RZjbOoyjRaWTEYM-cQOT53PsAUkDEqjXS1psR-QVZpPsJmChX_fTaxnFOSV')

  url = "https://api.spotify.com/v1/me/player/currently-playing"

  payload={}
  headers = {
    'Authorization': 'Bearer BQDb7skcTRBfg-dzNAoBB1qfeNXlboYCax_UOR5v90UhJLDH9dNtAexWFi2_Zp0UdgYvoM2FH21kwHcUbnOiasbr5dSs4njLuT2-EBKlDnmHcdCbKo246ReSThfQvvr10-y6mdiX-LSYxW7xrGg1CcATNyPii-8AyH2iGXRgHv6MPYpKY3mUMvYc7A'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  # print(response)
  # print(response.text)
  responseParams=json.loads(response.text)
  # print(responseParams["item"].keys())
  try:
    if responseParams["item"]["name"] != songName:
      songName = responseParams["item"]["name"]
      artistName = responseParams["item"]["artists"][0]["name"]
      getLyrics(songName, artistName, genius)
  except:
    print("SORRY, THE LYRICS ARE NOT AVIALBLE FOR THIS SONG")

  # print(songName, artistName)


def getLyrics(songName, artistName, genius):
  song = genius.search_song(songName, artistName)
  print("==================================\n"+songName, artistName+"\n"+song.lyrics)

if __name__=='__main__':
  while True:
    getSongDetails()
    time.sleep(5)


