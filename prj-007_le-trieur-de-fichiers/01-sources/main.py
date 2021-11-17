from pathlib import Path

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

"""
EXTENSIONS_DEF = {  ".mp3": "Musique",
                    ".wav": "Musique",
                    ".flac": "Musique",
                    ".mp4": "Videos",
                    ".avi": "Videos",
                    ".gif": "Videos",
                    ".bmp": "Images",
                    ".png": "Images",
                    ".jpg": "Images",
                    ".txt": "Documents",
                    ".pptx": "Documents",
                    ".csv": "Documents",
                    ".xls": "Documents",
                    ".odp": "Documents",
                    ".pages": "Documents"}


fichier_data = Path('01-sources/data')

# On récupère tous les fichiers dans le dossier de base
files = [f for f in fichier_data.iterdir() if f.is_file()]
for file in files:  # On boucle sur chaque fichier
    # On récupère le dossier cible à partir du dictionnaire
    dossier_cible = EXTENSIONS_DEF.get(file.suffix, "Divers")
    # On concatène le dossier de base avec le dossier cible
    dossier_cible_absolu = fichier_data / dossier_cible
    # On crée le dossier cible s'il n'existe pas déjà
    dossier_cible_absolu.mkdir(exist_ok=True)
    # On concatène le dossier cible avec le nom du fichier
    fichier_cible = dossier_cible_absolu / file.name
    # On déplace le fichier
    file.rename(fichier_cible)
