def score(x, y):
    pass
    distance_squared = x**2 + y**2
    
    # Define the squared radii for comparison
    RADIUS_1_SQUARED = 1**2   # 1 (Inner Circle)
    RADIUS_5_SQUARED = 5**2   # 25 (Middle Circle)
    RADIUS_10_SQUARED = 10**2 # 100 (Outer Circle / Max Target)

    # 2. Use conditional logic, checking the smallest (highest score) circle first.
    
    if distance_squared <= RADIUS_1_SQUARED:
        # Distance <= 1: Inner Circle
        return 10
    
    elif distance_squared <= RADIUS_5_SQUARED:
        # 1 < Distance <= 5: Middle Circle
        return 5
        
    elif distance_squared <= RADIUS_10_SQUARED:
        # 5 < Distance <= 10: Outer Circle
        return 1
        
    else:
        # Distance > 10: Outside the target
        return 0