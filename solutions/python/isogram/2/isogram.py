

def is_isogram(word: str) -> bool:
    """
    Determine if a given word or phrase is an isogram.

    Args:
        word (str): Input string to check.

    Returns:
        bool: True if no repeating letters (spaces and hyphens ignored).
    """
    clean_letters = [char for char in word.lower() if char.isalpha()]
    return len(clean_letters) == len(set(clean_letters))
    pass
    