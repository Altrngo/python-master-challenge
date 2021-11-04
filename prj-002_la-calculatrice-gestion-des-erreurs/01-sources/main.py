"""
Dans ce projet, vous devez réaliser une calculatrice en ligne de commande qui vous permettra d'additionner deux nombres ensemble.

👉 Déroulé du script
Le script doit demander à l'utilisateur de saisir deux nombres :

>>> Entrez un premier nombre : 5
>>> Entrez un deuxième nombre : 10
Le script doit ensuite afficher la phrase suivante :

"Le résultat de l'addition de 5 avec 10 est égal à 15"

Vous devrez donc utiliser une fonction de Python qui permet de récupérer la saisie de l'utilisateur (deux fois), pour ensuite additionner ces variables et afficher le résultat.

Vous devez vous assurer que le programme ne retournera pas d'erreur si l'utilisateur rentre autre chose que deux nombres.

Il va donc falloir gérer ces cas de figure. Si l'utilisateur rentre une lettre, un symbole ou quoi que ce soit d'autre qu'un nombre, vous devrez lui demander de nouveau de saisir deux valeurs valides :

>>> Entrez un premier nombre : a
>>> Entrez un deuxième nombre : sgoind
Veuillez entrer deux nombres valides
>>> Entrez un premier nombre
"""
a = ""
b = ""

while a.isdigit() == False or b.isdigit() == False:
  a = input("Veuillez entrer un premier nombre : ")
  b = input("Veuillez entrer un second nombre : ")

  if a.isdigit() == False or b.isdigit() == False:
    print("Veuillez entre deux nombres valides")

resultat = int(a) + int(b)

print(f"Le résultat de l'addition de {a} avec {b} est égal à {resultat}")