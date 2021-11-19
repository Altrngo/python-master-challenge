"""
Dans cet exercice vous devez :
- Ouvrir le fichier prenoms.txt et lire son contenu.
- Récupérer chaque prénom séparément dans une liste.
- Nettoyer les prénoms pour enlever les virgules, points ou espace.
- Écrire la liste ordonnée et nettoyée dans un nouveau fichier texte.
"""
from pprint import pprint

# Ouvrir le fichier et le parcourir
with open("prenoms.txt", "r") as f:
  lines = f.read().splitlines()
  # pprint(lines)

# creer la liste de prenoms
prenoms = []
for line in lines:
  prenoms.extend(line.split())
# pprint(prenoms)

# Cleaner les prenoms de leur virgule, point ou espace
liste_prenoms = [prenom.strip(",.") for prenom in prenoms]
# print (liste_prenoms)

# ecrire cette liste triée dans un fichier
with open("prenoms_final", "w") as f:
  f.write("\n".join(sorted(liste_prenoms)))
