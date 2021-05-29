name = input("What is your name?")
print("Your name is %s." % name)

age = input("What is your age?")
age = int(age)
print("Your age is %s." % age)

currentYear = 2021
missingYears = 100 - age
year100 = currentYear + missingYears

answer = "%s, you will be 100 years old in year %s." % (name, year100)
print(answer)

# Extra 1
multiplication = int(input("Pick a number."))
print(multiplication * answer)

# Extra 2
print(multiplication * (answer + "\n"))
