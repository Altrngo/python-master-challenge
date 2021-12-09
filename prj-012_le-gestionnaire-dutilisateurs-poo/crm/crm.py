import re
import string
from pathlib import Path

from tinydb import TinyDB, where, table


class User:
  
  DB = TinyDB(Path(__file__).resolve().parent/"db.json", indent=4)
  
  def __init__(self, first_name: str, last_name: str, phone_number: str="", address: str=""):
      self.first_name = first_name
      self.last_name = last_name
      self.phone_number = phone_number
      self.address = address

# Methode repr pour avoir une représentation de notre classe.
  def __repr__(self):
      return f"User ({self.first_name}, {self.last_name}) "

# Metohde pour afficher notre user sous forme de chaine de caractère.
  def __str__(self) -> str:
      return f"{self.full_name}\n{self.phone_number}\n{self.address}"

# Cette propriété nous permet d'avoir accés au nom complet du user sans avoir besoin de concatener a chaque fois le nom et le prenom.
  @property
  def full_name(self):
    return f"{self.first_name} {self.last_name}"

  @property
  def db_instance(self) -> table.Document:
    return User.DB.get((where("first_name") == self.first_name) & (where("last_name") == self.last_name))

  def _checks(self):
    self._check_names()
    self._check_phone_number()

  def _check_phone_number(self):
    phone_number = re.sub(r"[+()\s]*", "", self.phone_number)
    if len(phone_number) < 10 or not phone_number.isdigit():
      raise ValueError(f"Numero de telephone {self.phone_number} invalide.")

  def _check_names(self):
    if not (self.first_name and self.last_name):
      raise ValueError("Le prenom et le nom de famille ne peuvent pas être vides")
    
    special_caracters = string.punctuation+string.digits
    
    for caracter in self.first_name+self.last_name:
      if caracter in special_caracters:
        raise ValueError(f"Nom invalide : {self.full_name}")


  def exists(self):
    return bool(self.db_instance)

  def delete(self):
    if self.exists():
      return User.DB.remove(doc_ids=[self.db_instance.doc_id])
    return []


  def save(self, validate_data: bool = False) -> int:
    if validate_data:
      self._checks()
    
    if self.exists():
      return -1
    else:
      User.DB.insert(self.__dict__)
  

def get_all_users():
  # sous forme de comprehension de liste
  return [User(**user) for user in User.DB.all()]
  # sous forme de boucle
  # for user in User.DB.all():
  #   each_user = User(**user)
    # print(each_user.phone_number)
    
  
  
if __name__ == "__main__":
  eric = User("Eric", "Mayor")
  print(eric.db_instance)
  print (get_all_users())
  from faker import Faker
  fake = Faker(locale="fr_CH")
  for _ in range(10):
    user = User(first_name = fake.first_name(), 
                last_name = fake.last_name(),
                phone_number = fake.phone_number(),
                address = fake.address())
    print(user.save())
    # print(repr(user))
    print("-"*10)