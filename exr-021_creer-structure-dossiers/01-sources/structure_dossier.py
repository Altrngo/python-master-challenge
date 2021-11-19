from genericpath import exists
import os
from pathlib import Path


chemin = "dossier_test"

d = {"Films": ["Le seigneur des anneaux",
			   "Harry Potter",
			   "Moon",
			   "Forrest Gump"],
	 "Employes": ["Paul",
	 		      "Pierre",
				  "Marie"],
	 "Exercices": ["les_variables",
	 			   "les_fichiers",
				   "les_boucles"]}
           
          
# for key, value in d.items():
#   for dossier in value:
#     chemin_dossier = os.path.join(chemin, key, dossier)
#     os.makedirs(chemin_dossier, exist_ok=True)

# With Pathlib

for dossier_principal, sous_dossiers in d.items():
  for dossier in sous_dossiers:
    chemin_dossier = Path(chemin) / dossier_principal / dossier
    # print(chemin_dossier)
    chemin_dossier.mkdir(exist_ok=True, parents=True)