import random


# Wave 1
VALID_LETTERS = {'R', 'O', 'Y', 'G', 'B', 'P'}

def generate_code():
    valid_letters = list(VALID_LETTERS)
    # Generate a code of 4 random letters from valid_letters
    return [random.choice(valid_letters) for _ in range(4)]


def validate_guess(guess):
    valid_letters = VALID_LETTERS

    # Exit early if guess is not exactly 4 elements long
    if len(guess) != 4:
        return False
    
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)
    # Return False if we find an invalid element of guess
    for letter in uppercased_guess:
        if letter not in valid_letters:
            return False
        
    return True


def check_code_guessed(guess, code):
    # Convert guess to uppercase for case-insensitive comparison
    uppercased_guess = normalize_code(guess)
    # Check if the guess and code are identical (win condition)
    return code == uppercased_guess


def normalize_code(code):
    """Return a new list with the same order but with uppercased letters."""
    return [str(letter).upper() for letter in code]

# Wave 2
# Add your Wave 2 functions here


# Wave 3
# Add your Wave 3 functions here