from faker import Faker

fake = Faker(locale="fr_CH")

print(fake.name())
print(fake.address())