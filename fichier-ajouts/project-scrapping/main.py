import requests
from pprint import pprint
from bs4 import BeautifulSoup

def extract_lyrics(url):
  print("Fetching Lyrics...")
  r = requests.get(url)
  if r.status_code != 200:
    print("Page impossible a recuperer.")
    return []
  
  soup = BeautifulSoup(r.content, "html.parser")
  lyrics = soup.find("div", class_="lyrics")
  if not lyrics:
    return extract_lyrics(url)
  

def get_all_ulrs():
  
  page_number = 1
  links = []
  while True:
    r = requests.get(f'https://genius.com/api/artists/29743/songs?page={page_number}&sort=popularity')
    if r.status_code == 200:
      response = r.json().get("response", {})
      next_page = response.get("next_page")
      
      songs = response.get("songs")
      links.extend([song.get("url") for song in songs])
    
      page_number += 1
    
      if not next_page:
        print("No more pages to fetch.")
        break

  pprint(links)
  print(len(links))
    
get_all_ulrs()