def convert(number):
    """
    Converts a number into its corresponding raindrop sounds (Pling, Plang, Plong) 
    based on divisibility by 3, 5, and 7.
    """
    
    # Start with an empty string to accumulate the sounds.
    raindrops = ""

    # Check for divisibility by 3.
    # We use independent 'if' statements so we can add multiple sounds.
    if number % 3 == 0:
        raindrops += "Pling"
        
    # Check for divisibility by 5.
    if number % 5 == 0:
        raindrops += "Plang"
        
    # Check for divisibility by 7.
    if number % 7 == 0:
        raindrops += "Plong"

    # If the string is empty, it means the number was not divisible by 3, 5, or 7.
    # In that case, we return the original number as a string.
    if not raindrops:
        return str(number)
    else:
        return raindrops