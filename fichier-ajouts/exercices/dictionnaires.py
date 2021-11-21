films = {
  "Le Seigneur des Anneaux": 12,
  "Harry Potter": 9,
  "Blade Runner": 7.5
}

total = 0
for key in films:
  total += films[key]
  
print(total)

employes = {
            "id01": {"prenom": "Paul", "nom": "Dupont", "age": 32},
            "id02": {"prenom": "Julie", "nom": "Dupuit", "age": 25},
            "id03": {"prenom": "Patrick", "nom": "Ferrand", "age": 36}
            }

employes["id02"].update({"age" : 26 })
final = employes.pop("id03")
age_paul = (employes["id01"].get("age"))

# Correction
del employes["id03"]
employes["id02"]["age"] = 26
age_paul = employes["id01"]["age"]

