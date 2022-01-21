"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!!!!! GANG SHIT BRUHHHHH")
else:  
    print("man... you dumb as hell")
    if guess > SECRET:
        print("you too damn high")
    else:
        print("too low fucker")

print("Game over. Bitch.")
