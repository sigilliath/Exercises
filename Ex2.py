x = int(input("Type a number:"))

if x % 2 == 0:
    print("This number is even.")
else:
    print("This number is odd.")

# Extra 1
if x % 4 == 0:
    print("This number is a multiple of 4.")

# Extra 2
print("Now please type two numbers.")
num = int(input("First:"))

check = int(input("Second:"))

if num % check == 0:
    print("Your first number is divisible by your second number.")
else:
    print("Your second number is not divisible by your second number.")
