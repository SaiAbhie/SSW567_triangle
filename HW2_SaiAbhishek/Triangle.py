# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):
    """
    Classifies the type of triangle based on the lengths of its sides.

    Args:
    a (int): Length of the first side
    b (int): Length of the second side
    c (int): Length of the third side

    Returns:
    str: The type of triangle or 'InvalidInput'/'NotATriangle' for invalid cases.
    """
    
    # Input Validation: sides must be positive integers <= 200
    if not(isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
    
    # Triangle Inequality Theorem: the sum of any two sides must be greater than the third side
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'
    
    # Check for Equilateral: all three sides are equal
    if a == b == c:
        return 'Equilateral'
    
    # Check for Right Triangle: Pythagoras' theorem (a^2 + b^2 == c^2, etc.)
    # Sorting helps avoid confusion on which side is the hypotenuse
    sides = sorted([a, b, c])
    if (sides[0]**2 + sides[1]**2) == sides[2]**2:
        return 'Right'
    
    # Check for Isosceles: exactly two sides are equal
    if a == b or b == c or a == c:
        return 'Isosceles'
    
    # If no sides are equal, it's Scalene
    return 'Scalene'
