def getnum():
    return int(input("How many Fibonacci numbers should the program generate? "))


def genfibs(x):
    a = 0
    b = 1
    fibs = [a, b]
    count = 0
    while count < x-2:
        c = a + b
        fibs.append(c)
        a = b
        b = c
        count += 1
    return fibs


print(genfibs(getnum()))
