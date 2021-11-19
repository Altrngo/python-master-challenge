fichier = input("Entrez un fichier à ouvrir : ")

# Valid --> "/home/altrngo/code/Altrngo/python-master-challenge/exr-025_gerer-erreurs-fichier/01-sources/readme.txt"

# Invalid --> "/home/altrngo/code/Altrngo/python-master-challenge/exr-025_gerer-erreurs-fichier/01-sources/fichier_invalide.abc"

try:
  with open(fichier, "r") as f:
    lines = f.readlines()
    print(lines)
except UnicodeDecodeError as e:
  print("Erreur:", e)
except FileNotFoundError as e:
  print("Erreur: Ce fichier est introuvable")
else:
  f.close()
  print("Opération terminée")