import random
a = random.sample(range(100), 10)
b = random.sample(range(100), 10)
c = list(set([x for x in a for y in b if x == y]))

print(a)
print(b)
print(c)
