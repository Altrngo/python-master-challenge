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


