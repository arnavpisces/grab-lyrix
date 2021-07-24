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
    'Authorization': 'Bearer BQASidhB-68CEQBL94zTwpSCnJ_VwfVNWFI8ZIR_jIyJ8g9UIqDwlg8ZYk60tSfZ8xH1UydpqTsR3HaDiF06LHhCL5nGUbYimL8JlauQETMYn_pdr2nq_ugA6a7UigqvrnsBpeFhqw5htRnGuKXZEHVe0aqBpuGbShTwccmTRL6-EAHYPl6qNLsUPw'
  }
  response = requests.request("GET", url, headers=headers, data=payload)
  # print(response)
  # print(response.text)
  responseParams=json.loads(response.text)
  # print(responseParams["item"].keys())
  try:
    if responseParams["item"]["name"] != songName:
      print(songName, artistName)
      songName = responseParams["item"]["name"]
      artistName = responseParams["item"]["artists"][0]["name"]
      getLyrics(songName, artistName, genius)
  except:
    print("SORRY, THE LYRICS ARE NOT AVIALBLE FOR THIS SONG")



def getLyrics(songName, artistName, genius):
  song = genius.search_song(songName, artistName)
  print("==================================\n"+songName, artistName+"\n"+song.lyrics)

if __name__=='__main__':
  while True:
    getSongDetails()
    time.sleep(5)


