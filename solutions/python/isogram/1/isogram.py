def is_isogram(string):
    string = string.lower()
    filtered = [c for c in string if c.isalpha()]  # Use 'string' here, not 's'
    return len(filtered) == len(set(filtered))
    pass
    