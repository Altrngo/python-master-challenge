import os

chemin = "/home/altrngo/code/Altrngo/python-master-challenge/chp-003_quelques-modules-et-fonctions/le-module-os"
dossier = os.path.join(chemin, "dossier", "test")
if os.path.exists(dossier):
# os.makedirs(dossier)
  os.removedirs(dossier)
print(dossier)