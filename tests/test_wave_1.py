from app.game import generate_code, validate_guess, check_code_guessed

# --------------------------test generate_code------------------------------------

def test_generate_code_length_four():
    # Arrange/Act
    result = generate_code()

    # Assert
    assert len(result) == 4

    
def test_generate_code_returns_list():
    #Arrange/Act
    result = generate_code()

    #Assert
    assert isinstance(result, list)


def test_generate_code_uses_valid_letters():
    # Arrange
    valid_letters = {'R', 'O', 'Y', 'G', 'B', 'P'}

    # Act
    result = generate_code()

    # Assert
    for letter in result:
        assert letter in valid_letters

def test_generate_code_half_or_less_duplicates_over_10_runs():
    runs = 10
    results = [tuple(generate_code()) for _ in range(runs)]
    unique_results = set(results)
    assert len(unique_results) > runs / 2        

# --------------------------test validate_guess------------------------------------

def test_validate_guess_false_length_greater_than_four():
    # Arrange
    guess = ['R', 'R', 'R', 'R', 'R']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_valid_letters_rygp():
    # Arrange
    guess = ['R', 'Y', 'G', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_true_valid_letters_bp():
    # Arrange
    guess = ['B', 'B', 'P', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_false_invalid_letters():
    # Arrange
    guess = ['R', 'S', 'Y', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_lowercase_letters():
    # Arrange
    guess = ['b', 'b', 'p', 'p']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True


def test_validate_guess_false_not_a_list_string():
    # Arrange
    guess = 'RBYG'  # not a list

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_not_a_list_tuple():
    # Arrange
    guess = ('R', 'B', 'Y', 'G')  # tuple, not list

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_length_less_than_four():
    # Arrange
    guess = ['R', 'B', 'Y']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_element_not_string():
    # Arrange
    guess = ['R', 'B', 1, 'G']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_element_empty_string():
    # Arrange
    guess = ['R', '', 'Y', 'G']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_false_element_multi_char():
    # Arrange
    guess = ['RR', 'B', 'Y', 'G']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is False


def test_validate_guess_true_mixed_case_letters():
    # Arrange
    guess = ['r', 'G', 'y', 'P']

    # Act
    result = validate_guess(guess)

    # Assert
    assert result is True

# # --------------------------test check_win_or_lose------------------------------------

def test_check_code_guessed_true():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is True


def test_check_code_guessed_no_match_false():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'O']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False


def test_check_code_guessed_true_mixed_case_guess():
    # Arrange
    guess = ['r', 'b', 'B', 'p']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is True


def test_check_code_guessed_false_guess_not_list():
    # Arrange
    guess = 'RBBP'  # not a list
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False


def test_check_code_guessed_false_code_not_list():
    # Arrange
    guess = ['R', 'B', 'B', 'P']
    code = ('R', 'B', 'B', 'P')  # not a list

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False


def test_check_code_guessed_false_length_mismatch():
    # Arrange
    guess = ['R', 'B', 'B']  # length 3
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False


def test_check_code_guessed_false_element_not_string():
    # Arrange
    guess = ['R', 'B', None, 'P']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False


def test_check_code_guessed_false_element_multi_char():
    # Arrange
    guess = ['RR', 'B', 'B', 'P']
    code = ['R', 'B', 'B', 'P']

    # Act
    result = check_code_guessed(guess, code)

    # Assert
    assert result is False
