def is_pangram(sentence):
    # 1. Initialization and Standardization
    unique_letters = set()
    sentence_lower = sentence.lower()
    
    # 2. Iteration, Filtering, and Collection
    for char in sentence_lower:
        if char.isalpha():
            unique_letters.add(char)
            
    # 3. Final Check (Validation)
    return len(unique_letters) == 26