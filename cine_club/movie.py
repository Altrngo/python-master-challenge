import os
import json
import logging

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")
# print(DATA_FILE)

def get_movies():
  with open(DATA_FILE, "r") as f:
    movies_title = json.load(f)
  
  movies = [Movie(movie_title) for movie_title in movies_title]
  return movies



class Movie:
  def __init__(self, title):
    self.title = title.title()

  
  def __str__(self):
    return self.title
  
  def _get_movies(self):
    with open(DATA_FILE, "r") as f:
      return json.load(f)
      
  
  def _write_movies(self, movies):
    with open(DATA_FILE, "w") as f:
      json.dump(movies, f, indent=4)
  
  def add_to_movies(self):
    # Recuperer la liste des films
    movies = self._get_movies()
    
    # Verifier que le film n'est pas deja dans la liste
    if self.title not in movies:
      movies.append(self.title)
    # Si ce n'est pas le cas on l'ajoute
      self._write_movies(movies)
      return True
    # Si c'est le cas, on affiche un message pour indiquer que le film est deja present (avec le module logging.)
    else:
      logging.warning(f"Le film {self.title} est déjà enregistré.")
      return False

  
  def remove_from_movies(self):
    movies = self._get_movies()
    
    if self.title in movies:
      movies.remove*(self.title)
      self._write_movies(movies)
      
  
if __name__ == "__main__":
  movies = get_movies()
  print(movies)