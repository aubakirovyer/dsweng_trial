from math import pi

def calculate_squre_area(a: int) -> int:
    """Calculate the area of a square given the length of one side."""
    return a * a

def calculate_rectangle_area(length: int, width: int) -> int:
    """Calculate the area of a rectangle given its length and width."""
    return length * width

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius."""
    return pi * (radius ** 2)