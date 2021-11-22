"""Module to generate random users"""
import faker
import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
logging.basicConfig(filename=BASE_DIR / "user.log", level=logging.INFO)

fake = faker.Faker("fr_CH")


def get_user():
  """Generate a Single user

  Returns:
      [str]: [user]
  """
  logging.info("Generating user.")
  return f"{fake.first_name()} {fake.last_name()}"


def get_users(n):
  """[Generate a list of users]

  Args:
      n ([int]): [number of user to generate]

  Returns:
      list[str]: [users]
  """
  logging.info(f"Generating a list of {n} user.")
  # avec une comrehension de liste
  return[get_user() for _ in range(n)]
  
  # avec une boucle:
  # users = []
  # for i in range(n):
  #   users.append(get_user())
    
  return users

if __name__ == "__main__":
  user = get_users(n=5)
  print(user)
  
