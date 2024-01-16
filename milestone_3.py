from milestone_2 import word


def check_guess(guess):
    guess_lowered = guess.lower()
    if guess_lowered in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")


def ask_for_input():
    while True:
        guess = input("Please take a guess: ")

        if (guess.isalpha() == False) or len(guess) > 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            break

    check_guess(guess)


ask_for_input()
