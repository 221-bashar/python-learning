def reverse(text):
    # Initialize an empty list
    reversed_chars = []
    
    # 2. Loop backward from the last index to 0
    # Note: 'for' loop is correctly indented once
    for i in range(len(text) - 1, -1, -1):
        # 3. Append the character using the correct variable name 'text'
        # Note: This line is correctly indented twice
        reversed_chars.append(text[i])
        
    # 4. Join the list of characters back into a single string
    # Note: 'return' is correctly indented once
    return "".join(reversed_chars)
