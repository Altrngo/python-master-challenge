import logging

LOGGER = logging.getLogger()


class Liste(list):
    def __init__(self, nom):
        self.nom = nom

    def ajouter(self, element):
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaînes de caractères!")
        
        if element in self:
            LOGGER.error(f"{element} est déjà dans la liste.")
            return False

        self.append(element)
        return True

    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False

if __name__ == "__main__":
    liste = Liste("courses")
    liste.ajouter("Pommes")
    liste.ajouter("Poires")
    print(liste)
    
liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
trois_derniers = liste[-3:]
milieu = liste[1:-1]
premier_dernier = liste[0::5]

print(trois_premiers)
print(trois_derniers)
print(milieu)
print(premier_dernier)

liste = [1, 2, 3, 4, 5]
liste.append(6)

if 6 in liste:
    print("Le nombre 6 a bien été ajouté a la liste")      