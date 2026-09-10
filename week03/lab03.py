import random


def generate_mad_lib(adjective, noun, verb):
    """Return a nonempty story containing all three supplied words."""
    return f"The {adjective} {noun} {verb} over the lazy dog."


def guessing_game():
    """Run an interactive number-guessing game."""
    secret_number = random.randint(1, 100)

    while True:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break