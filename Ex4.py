x = int(input("Give me a number: "))

answ = []

for num in range(1, x+1):
    if x % num == 0:
        answ.append(num)

print("The divisors of " + str(x) + " are:")
print(answ)