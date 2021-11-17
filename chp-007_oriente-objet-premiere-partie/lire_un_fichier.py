import json

chemin = "/home/altrngo/code/Altrngo/python-master-challenge/chp-007_oriente-objet-premiere-partie/fichier.txt"

# f = open(chemin, "r")
# f.close()

# with open(chemin, "r") as f:
#   contenu = f.readlines()
#   print (contenu)

# with open(chemin, "r") as f:
#   contenu = f.read().splitlines()
#   print (contenu)

# with open(chemin, "a") as f:
#   f.write("\nAu revoir")
  
chemin_json = "/home/altrngo/code/Altrngo/python-master-challenge/chp-007_oriente-objet-premiere-partie/test.json"
  
with open(chemin_json, "w") as f:
  json.dump(list(range(3)), f, indent=2)
  
    
# with open(chemin_json, "r") as f:
#   liste = json.load(f)
#   print(type(liste))
  
with open(chemin_json, "r") as f:
  donnees = json.load(f)
  
donnees.append(4)

with open(chemin_json, "w") as f:
  json.dump(donnees, f, indent=4)