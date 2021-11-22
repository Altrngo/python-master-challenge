import faker

fake = faker.Faker("fr_CH")

def get_user():
  return f"{fake.first_name()} {fake.last_name()}"

def get_users(n):
  
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
  
