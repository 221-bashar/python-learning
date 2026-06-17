def response(hey_bob):
    # Fix the Indentation for all lines below!
    trimmed_input = hey_bob.strip()

    # Yelling a Question (Most Specific)
    if trimmed_input.endswith('?') and trimmed_input.isupper():
        return "Calm down, I know what I'm doing!"

    # Yelling (Next Specific)
    # Be careful not to count empty strings or questions as yelling!
    elif trimmed_input.isupper():
        return "Whoa, chill out!"
    
    # Question (Next Specific)
    elif trimmed_input.endswith('?'):
        return "Sure."
        
    # Silence
    elif trimmed_input == '':
        return "Fine. Be that way!"

    # Anything Else
    else:
        return "Whatever."
