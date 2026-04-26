def is_valid(isbn: str) -> bool:
    # Remove hyphens
    clean = isbn.replace("-", "")
    
    # ISBN-10 must be exactly 10 characters
    if len(clean) != 10:
        return False
    
    # Check all but last are digits
    if not all(ch.isdigit() for ch in clean[:-1]):
        return False
    
    # Last character can be digit or 'X'/'x' (meaning 10)
    if not (clean[-1].isdigit() or clean[-1].upper() == 'X'):
        return False
    
    total = 0
    for i, ch in enumerate(clean):
        if i == 9 and ch.upper() == 'X':  # last char 'X' means 10
            value = 10
        else:
            value = int(ch)
        total += (i + 1) * value
    
    # Valid if total divisible by 11
    return total % 11 == 0
    pass
