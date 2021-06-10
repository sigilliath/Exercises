import random

score = 0


def credits():
    print("Thanks for playing! You guessed right %d numbers!" % score)
    exit()


while True:
    a = random.randint(1, 9)
    guess = input("Guess a number 1-9 or write 'exit' to quit: ").lower()
    if guess == "exit":
        credits()
    while int(guess) != a:
        if int(guess) > a:
            print("Your number is too high.")
            guess = input("Guess a number 1-9 or write 'exit' to quit: ").lower()
            if guess == "exit":
                credits()
                pass
        elif int(guess) < a:
            print("Your number is too low.")
            guess = input("Guess a number 1-9 or write 'exit' to quit: ").lower()
            if guess == "exit":
                credits()
            pass
        elif int(guess) == "exit":
            break
    print("Congratulations! you guessed %d!" % a)
    score += 1
    print("You guessed %d numbers right!" % score)
