"""Module to verify validity of ISBN-10 numbers."""

def is_valid(isbn: str) -> bool:
    """
    Check if the given ISBN-10 string is valid.

    Args:
        isbn (str): ISBN number potentially containing hyphens.

    Returns:
        bool: True if ISBN is valid, else False.
    """
    # Remove hyphens for clean processing
    clean_isbn = isbn.replace("-", "")

    # ISBN-10 must be exactly 10 characters
    if len(clean_isbn) != 10:
        return False

    # Ensure first nine characters are digits
    if not all(character.isdigit() for character in clean_isbn[:-1]):
        return False

    # Last character can be a digit or 'X'/'x' denoting 10
    last_char = clean_isbn[-1]
    if not (last_char.isdigit() or last_char.upper() == "X"):
        return False

    total_sum = 0
    for position, character in enumerate(clean_isbn):
        if position == 9 and character.upper() == "X":
            value = 10
        else:
            value = int(character)
        total_sum += (position + 1) * value

   
# Valid if total_sum divisible by 11
    return total_sum % 11 == 0
