import random

"""
Le but de ce projet est de permettre à un joueur d'essayer de deviner un nombre mystère généré aléatoirement par l'ordinateur, en 5 essais ou moins.

👉 Déroulé du script
Au début du script, vous devez générer un nombre aléatoire compris entre 0 et 100 (vous pouvez agrandir ou réduire cet intervalle pour simplifier ou complexifier le jeu).

Le joueur dispose alors de 5 essais (là encore, libre à vous de changer cette valeur) pour trouver le nombre mystère.

À chaque essai, vous devez indiquer au joueur si le nombre qu'il a entré est plus petit ou plus grand que le nombre mystère.

Si le nombre entré par l'utilisateur est égal au nombre mystère, alors le joueur gagne la partie.

Dans le cas d'une victoire, vous devez indiquer au joueur combien d'essais lui ont été nécessaire pour gagner.

Si le joueur ne trouve pas le nombre mystère avec les 5 essais disponibles, il perd la partie.
"""


nombre_cpu = random.randint(1, 10)
user_choice = "-1"

def choix_nombre():
  count = 5
  while count >= 1:
    user_choice = input("Veuillez choisir un nombre : ")
    if user_choice.isdigit == False:
      print("Merci de rentrer un nombre !")
    else:
      count-=1
      if int(user_choice) == nombre_cpu:
        print(f"VOUS AVEZ GAGNE (en {5-count} coups) !!!")
      elif int(user_choice) < nombre_cpu and count > 0:
        print(f"Trop bas ! Encore {count} essais")
      elif int(user_choice) > nombre_cpu and count > 0:
        print(f"Trop haut ! Encore {count} essais")
  else:
    print("vous avez perdu !")
    print(f"Le nombre était {nombre_cpu}")


choix_nombre()

# Comparer le chiffre user avec le chiffre CPU

# Victoire si nombre == / Defaite si nombres different

