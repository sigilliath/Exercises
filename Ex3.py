a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in a:
    if number < 5:
        print(number)

# Extra 1
aa = []
for number in a:
    if number < 5:
        aa.append(number)

print(aa)

# Extra 2
print([number for number in a if number < 5])

# Extra 3
x = int(input("Input any number:"))
aaa = []

for number in a:
    if number < x:
        aaa.append(number)

print(aaa)
