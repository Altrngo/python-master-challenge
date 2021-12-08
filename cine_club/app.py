import typing
import PySide2
from PySide2 import QtWidgets, QtCore
from movie import get_movies

class App(QtWidgets.QWidget):
  def __init__(self):
    super().__init__
    self.setWindowTitle("Ciné Club")
    self.setup_ui()
    self.populate_movies()

  def setup_ui(self):
    self.main_layout = QtWidgets.QVBoxLayout(self)
    
    self.le_movieTitle = QtWidgets.QLineEdit()
    self.btn_addMovie = QtWidgets.QPushButton("Ajouter un film")
    self.lw_movies = QtWidgets.QListWidget()
    self.btn_removeMovies = QtWidgets. QPushButton("Supprimer le(s) film(s)")
    
    self.main_layout.addWidget(self.le_movieTitle)
    self.main_layout.addWidget(self.btn_addMovie)
    self.main_layout.addWidget(self.lw_movies)
    self.main_layout.addWidget(self.btn_removeMovies)

  def populate_movies(self):
    movies = get_movies()
    
    for movie in movies:
      self.lw_movies.addItem(movie.title)
      # ou alors plus compliqué mais plus pratique:
      # lw_item = QtWidgets.QListWidgetItem(movie.title)
      # lw_item.setData(QtCore.Qt.UserRole, movie)
      # self.lw_movies.addItem(lw_item)
    
    
app = QtWidgets.QApplication([])
win = App()
win.show()
app.exec_()