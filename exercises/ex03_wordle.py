"""Exercise 03 by Hayden Trayah."""

__author__ = "730325581"


def contains_char(searched_string: str, single_char: str) -> bool:
    """Searches parameter one for the presence of parameter two."""
    assert len(single_char) == 1
    found_in_word = False
    char_counter: int = 0
    while found_in_word is False and char_counter < len(searched_string):
        if searched_string[char_counter] == single_char:
            found_in_word = True
        else:
            char_counter = char_counter + 1
    if found_in_word is True:
        return True
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Assigns emojis based on character presence and location of guess's characters in secret."""
    assert len(guess) == len(secret)
    guess_index = 0
    index_emoji = str("")
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while guess_index < len(secret):
        if guess[guess_index] == secret[guess_index]:
            index_emoji = index_emoji + GREEN_BOX
            guess_index = guess_index + 1
        else:
            if contains_char(secret, guess[guess_index]) is True:
                index_emoji = index_emoji + YELLOW_BOX
            else:
                index_emoji = index_emoji + WHITE_BOX
            guess_index = guess_index + 1
    return index_emoji


def input_guess(guess_length: int) -> str:
    """Verifies that the length of the guess equals the length of the secret."""
    guess = input(f"Enter a {guess_length} character word: ")
    while len(guess) != guess_length:
        guess = str(input(f"That wasn't {guess_length} chars! Try again: "))
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    secret_word_length: int = len(secret_word)
    remaining_turns: int = 6
    turn_counter: int = 1
    won_game: bool = False
    while remaining_turns > 0 and won_game is False:
        print(f"=== Turn {turn_counter}/6 ===")
        user_input = (str((input_guess(secret_word_length))))
        print(emojified(user_input, secret_word))
        if user_input == secret_word:
            won_game = True
        else:
            remaining_turns = remaining_turns - 1
            turn_counter = turn_counter + 1
    if won_game is True:
        print(f"You won in {turn_counter}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()