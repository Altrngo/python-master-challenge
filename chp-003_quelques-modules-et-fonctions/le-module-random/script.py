import random
from pprint import pprint

r = random.randint(0, 1)
r = random.uniform(0, 1)
r = random.randrange(2)
r = random.randrange(0, 101, 10)

print(r)

help(random.randint)
# print(help(os.makedirs))
pprint(dir(random))