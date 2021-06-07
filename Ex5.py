a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []

for num in a:
    if num in b:
        if num in c:
            continue
        else:
            c.append(num)

print(c)

# Extra 1
import random

n = random.sample(range(1, 99), 15)
m = random.sample(range(1, 99), 15)

z = []

for num in n:
    if num in m:
        if num in z:
            continue
        else:
            z.append(num)

print(n)
print(m)
print(z)

# Extra 2

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = list(set(count for count in a if count in b))
print(c)
