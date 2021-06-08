# NADAL PRÓBUJĘ

possible = ("rock", "paper", "scissor")
print("This program lets you play 'rock, paper, scissor'!")
while input("Do you want to start new game? ").lower() == "yes":
    p1 = input("Player 1, what do you play? ").lower()
    while p1 not in possible:
        print("You must use 'rock', 'paper', or 'scissor'!")
        p1 = input("Player 1, what do you play? ").lower()
    p2 = input("Player 2, what do you play? ").lower()
    while p2 not in possible:
        print("You must use 'rock', 'paper', or 'scissor'!")
        p2 = input("Player 2, what do you play? ").lower()
    if p1 == p2:
        print("Draw!")
    elif p1 == "rock":
        if p2 == "paper":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    elif p1 == "paper":
        if p2 == "scissor":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    else:
        if p2 == "rock":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
else:
    print("Thanks for playing!")
