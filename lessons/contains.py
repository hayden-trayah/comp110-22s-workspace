"""Example of writing a function to search a list."""


def main() -> None:
    guess: str = input("What is the code word?")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club...")
    else:
        print("Go back to Davis.")

# Define a function named contains
# Parameters:
#   1. needle - the str we're searching for
#   2. haystack - the list of str values we're seraching through


def contains(needle: str, haystack: list[str]) -> bool:
    #  Algorithm: for each item in haystack:
    #       Test if equal to needle
    #           if so, return True
    """Test if needle is found in haystack."""
    for item in haystack:
        if item == needle:
            return True
#     After all itmes checked, that means needle is not found, return False
    return False
#  Returns True iff meedle is found in haystack


print(__name__)

if __name__ == "__main__":
    main()
# The reason we have this is to get the best of both words. We can import function definitions into other places without having the
# main function be evaluated. Without the idiom, if you import a function from a different module it will evaluate the program
# and execute the main function. This is python specfic.