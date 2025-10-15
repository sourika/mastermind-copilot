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

def _to_letter_list(x):
    """Helper: normalize input to a list of single uppercase letters.

    Accepts either a list[str] or a str. Other types are returned as-is
    (and will likely result in 0 matches downstream).
    """
    if isinstance(x, str):
        return [ch.upper() for ch in x]
    if isinstance(x, list):
        out = []
        for ch in x:
            if isinstance(ch, str) and len(ch) == 1:
                out.append(ch.upper())
        return out
    return x

def color_count(guess, code):
    """Return the number of pegs that are the correct color regardless of position.

    Rules:
    - Count a color at most as many times as it appears in BOTH guess and code.
    - Case-insensitive.
    - Accepts guess and code as list[str] or str.
    """
    g_list = _to_letter_list(guess)
    c_list = _to_letter_list(code)

    # If inputs aren't lists after normalization, no matches can be found
    if not isinstance(g_list, list) or not isinstance(c_list, list):
        return 0

    # Build frequency dictionaries without using Counter
    g_counts = {}
    for ch in g_list:
        g_counts[ch] = g_counts.get(ch, 0) + 1

    c_counts = {}
    for ch in c_list:
        c_counts[ch] = c_counts.get(ch, 0) + 1

    total = 0
    # Sum the intersection counts across all colors present in either
    colors = set(g_counts.keys()) | set(c_counts.keys())
    for color in colors:
        total += min(g_counts.get(color, 0), c_counts.get(color, 0))

    return int(total)

def correct_pos_and_color(guess, code):
    """Return the number of pegs that are the correct color AND in the correct position.

    Case-insensitive; accepts list[str] or str.
    """
    g_list = _to_letter_list(guess)
    c_list = _to_letter_list(code)
    if not isinstance(g_list, list) or not isinstance(c_list, list):
        return 0
    n = min(len(g_list), len(c_list))
    return sum(1 for i in range(n) if g_list[i] == c_list[i])

def check_guess(guess, code):
    """Return a tuple: (correct position & color, correct color only).

    The second value counts correct colors that are NOT in the correct position.
    """
    return generate_hint(guess, code)


def generate_hint(guess, code):
    """Return a tuple (both, color_only).

    - both: number of pegs correct in both color and position
    - color_only: number of pegs correct in color but wrong position

    Accepts guess and code as list[str] or str; comparison is case-insensitive.
    """
    both = correct_pos_and_color(guess, code)
    colors = color_count(guess, code)
    # Colors includes correctly positioned ones; subtract to get color-only
    return (int(both), max(0, int(colors) - int(both)))


# Wave 3
# Add your Wave 3 functions here


