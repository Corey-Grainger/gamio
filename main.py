"""
CP1404 - Guessing Game for review and refactor
Some of this is "good" code, but some things are intentionally poor
This is for a code review and refactoring exercise
"""

import math
import random

DEFAULT_LOW = 1
DEFAULT_HIGH = 10
MENU_PROMPT = "(P)lay, (S)et limit, (H)igh scores, (Q)uit: "


def main():
    """Run a menu-driven guessing game with option to change high limit."""
    high = DEFAULT_HIGH
    number_of_games = 0
    print("Welcome to the guessing game")
    choice = input(MENU_PROMPT).upper()
    while choice != "Q":
        if choice == "P":
            play(DEFAULT_LOW, high)
            number_of_games += 1
        elif choice == "S":
            high = set_high_limit(DEFAULT_LOW)
        elif choice == "H":
            display_scores()
        else:
            print("Invalid choice")
        choice = input(MENU_PROMPT).upper()
    print(f"Thanks for playing ({number_of_games} times)!")


def play(low, high):
    """Play guessing game using current low and high values."""
    secret = random.randint(low, high)
    number_of_guesses = 1
    guess = int(input(f"Guess a number between {low} and {high}: "))
    while guess != secret:
        number_of_guesses += 1
        if guess < secret:
            print("Higher")
        else:
            print("Lower")
        guess = int(input(f"Guess a number between {low} and {high}: "))
    print(f"You got it in {number_of_guesses} guesses.")
    if is_good_score(number_of_guesses, high - low + 1):
        print("Good guessing!")
    choice = input("Do you want to save your score? (y/N) ")
    if choice.upper() == "Y":
        save_score(number_of_guesses, low, high)
    else:
        print("Fine then.")


def save_score(number_of_guesses, low, high):
    """Save score to scores.txt with range."""
    with open("scores.txt", "a", encoding="UTF-8") as outfile:
        print(f"{number_of_guesses}|{high - low + 1}", file=outfile)


def set_high_limit(low):
    """Set high limit to new value from user input."""
    print("Set new limit")
    new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    while new_high <= low:
        print("Higher!")
        new_high = get_valid_number(f"Enter a new high value, above {low}: ")
    return new_high


def get_valid_number(prompt):
    """Get a valid number."""
    is_valid = False
    while is_valid is False:
        try:
            number = int(input(prompt))
            is_valid = True
        except ValueError:
            print("Invalid number")
    return number  # No error


def is_good_score(number_of_guesses, score_range):
    """Determine if score is good."""
    return number_of_guesses <= math.ceil(math.log2(score_range))


def display_scores():
    """Display scores with an ! beside high scores."""
    scores = load_scores()
    scores.sort()
    for score in scores:
        marker = "!" if is_good_score(score[0], score[1]) else ""
        print(f"{score[0]} ({score[1]}) {marker}")


def load_scores():
    """Load a list of scores."""
    with open("scores.txt", encoding="UTF-8") as in_file:
        scores = []
        for line in in_file:
            line = line.split("|")
            scores.append((int(line[0]), int(line[1])))
    return scores


main()
