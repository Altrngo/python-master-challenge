import sys
import os
import json

CUR_DIR = os.path.dirname(__file__)
LISTE_PATH = os.path.join(CUR_DIR, "liste.json")

action = 0
liste = []
menu_actions = """
Que souhaitez-vous faire ?

--------------------------------------
1 - Ajouter un élément à la liste de courses
2 - Retirer un élément de la liste de courses
3 - Afficher les éléments de la liste de courses
4 - Vider la liste de courses
5 - Quitter le programme
--------------------------------------

Entrer le numéro de l'action : """

liste_actions = ["1","2","3","4","5"]

if os.path.exists(LISTE_PATH):
  with open(LISTE_PATH, "r") as f:
    liste = json.load(f)
else:
  liste = []

while True:
  action = input(menu_actions)
  if action not in liste_actions:
    print("Merci de choisir une action dans la liste...")
    continue

  if action == "1":
    article = input("Entrer un article a ajouter : ")
    liste.append(article)
    print(f"L'article {article} a bien été ajouté.")
  elif action == "2":
    article = input("Entrer le numéro de l'article a supprimer : ")
    print(f"L'article {liste[int(article)-1]} a bien été supprimé de la liste.")
    liste.pop(int(article)-1)
  elif action == "3":
      print("Voici le contenu de votre liste :")
      for i, article in enumerate(liste, start=1):
        print(f"{i}. {article}")
  elif action == "4":
    liste.clear()
    print("Votre liste a été vidée.")
  elif action == "5":
    with open(LISTE_PATH, "w") as f:
      json.dump(liste, f, indent=4)
      print("Au revoir !")
      sys.exit()

"""
Le but de ce projet est de créer un script qui permette de trier automatiquement des fichiers dans des sous-dossiers en fonction de leur type (extension).

Dans les sources de ce projet, vous trouverez un dossier data qui contient des fichiers de différents types (images, vidéos, documents...).

Vous pouvez partir de ce dossier ou utiliser n'importe quel dossier de votre disque dur (le dossier de téléchargements est généralement un bon endroit pour faire le ménage...).

Le but de ce script est de trier les fichiers selon leur type (et donc leur extension) dans des sous-dossiers.

Par exemple, vous devez regrouper tous les fichiers avec l'extension .mp3 ou .wav dans un sous-dossier Musique.

Tous les fichiers textes quant à eux devront se retrouver dans un dossier Documents.

Voici l'association des extensions et des dossiers que vous devez utiliser :

mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
Le but de ce projet est de créer un script qui permette de trier automatiquement des fichiers dans des sous-dossiers en fonction de leur type (extension).

Dans les sources de ce projet, vous trouverez un dossier data qui contient des fichiers de différents types (images, vidéos, documents...).

Vous pouvez partir de ce dossier ou utiliser n'importe quel dossier de votre disque dur (le dossier de téléchargements est généralement un bon endroit pour faire le ménage...).

Le but de ce script est de trier les fichiers selon leur type (et donc leur extension) dans des sous-dossiers.

Par exemple, vous devez regrouper tous les fichiers avec l'extension .mp3 ou .wav dans un sous-dossier Musique.

Tous les fichiers textes quant à eux devront se retrouver dans un dossier Documents.

Voici l'association des extensions et des dossiers que vous devez utiliser :
- mp3, wav, flac : Musique
- avi, mp4, gif : Videos
- bmp, png, jpg : Images
- txt, pptx, csv, xls, odp, pages : Documents
- autres : Divers
"""


