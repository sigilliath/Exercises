print("This program checks if input number is a prime number.")
x = int(input("Give me a number: "))
div = range(1, x + 1)
answ = []
for num in div:
    if x % num == 0:
        answ.append(num)
if x == 0:
    print("0 is not prime nor composite. You cannot divide by 0!")
else:
    print("Number %d is a prime number!" % x) if len(answ) == 2 else print("Number %d is not a prime number!" % x)
