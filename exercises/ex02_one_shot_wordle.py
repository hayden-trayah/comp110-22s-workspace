"""Excercise 02 by Hayden Trayah."""

__author__ = "730325581"

secret = "python"
secret_length = len(secret)
guess = str(input(f"What is your {secret_length} letter guess? "))
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != secret_length:
    guess = str(input(f"That was not {secret_length} letters! Try again: "))

guess_index = 0
index_emoji = str("")

while guess_index < secret_length:
    if guess[guess_index] == secret[guess_index]:
        index_emoji = index_emoji + GREEN_BOX
        guess_index = guess_index + 1
    else:
        elsewhere_in_word = False
        alt_index = 0
        while elsewhere_in_word is False and alt_index < secret_length:
            if secret[alt_index] == guess[guess_index]:
                elsewhere_in_word = True
            else:
                alt_index = alt_index + 1
        if elsewhere_in_word is True:
            index_emoji = index_emoji + YELLOW_BOX
        else:
            index_emoji = index_emoji + WHITE_BOX
        guess_index = guess_index + 1

print(index_emoji)

if guess != secret:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")
