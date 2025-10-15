# Wave 1
def generate_code():
    import random
    letters = ['R', 'O', 'Y', 'G', 'B', 'P']
    return [random.choice(letters) for _ in range(4)]
# generate_code 
# - takes no arguments  
# - returns a list of 4 letters
# - each letter must be one of: R, O, Y, G, B, P

def validate_guess(guess):
    """Return True if guess is a list of length 4 containing only
    the letters R, O, Y, G, B, P (case-insensitive). Otherwise False.

    guess: list[str]
    """
    valid = {'R', 'O', 'Y', 'G', 'B', 'P'}

    # Must be a list of length 4
    if not isinstance(guess, list) or len(guess) != 4:
        return False

    # Every element must be a single character from the valid set (case-insensitive)
    for ch in guess:
        if not isinstance(ch, str) or len(ch) != 1:
            return False
        if ch.upper() not in valid:
            return False

    return True

def check_code_guessed(guess, code):
    """Return True if guess and code are the same combination regardless of case.

    Both guess and code should be lists of length 4 containing single-character strings.
    If inputs are malformed or lengths differ, return False.
    """
    # Basic structural checks
    if not isinstance(guess, list) or not isinstance(code, list):
        return False
    if len(guess) != 4 or len(code) != 4:
        return False

    # Compare element-wise; only uppercase guess assuming code is uppercase
    for g, c in zip(guess, code):
        if not isinstance(g, str) or not isinstance(c, str) or len(g) != 1 or len(c) != 1:
            return False
        if g.upper() != c:
            return False

    return True

# Wave 2
# Add your Wave 2 functions here

# Wave 3
# Add your Wave 3 functions here
