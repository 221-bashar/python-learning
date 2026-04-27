"""Module to determine triangle types based on side lengths."""

def is_triangle(sides):
    """Check if the sides form a valid triangle using the inequality theorem."""
    side_a, side_b, side_c = sides
    return (side_a > 0 and side_b > 0 and side_c > 0 and
            side_a + side_b >= side_c and
            side_b + side_c >= side_a and
            side_a + side_c >= side_b)

def equilateral(sides):
    """Return True if the triangle is equilateral."""
    if not is_triangle(sides):
        return False
    side_a, side_b, side_c = sides
    return side_a == side_b == side_c

def isosceles(sides):
    """Return True if the triangle is isosceles."""
    if not is_triangle(sides):
        return False
    side_a, side_b, side_c = sides
    return side_a == side_b or side_b == side_c or side_a == side_c

def scalene(sides):
    """Return True if the triangle is scalene."""
    if not is_triangle(sides):
        return False
    side_a, side_b, side_c = sides
    return side_a != side_b and side_b != side_c and side_a != side_c