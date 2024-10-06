def classifyTriangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the triangle.

    return:
        - 'Equilateral' if all three sides are equal
        - 'Isosceles' if exactly two sides are equal
        - 'Scalene' if no sides are equal
        - 'NotATriangle' if the inputs do not form a valid triangle
        - 'Right' if the triangle is a right triangle (Pythagorean theorem)
    """

    # Check for invalid inputs (sides should be integers between 0 and 200)
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    # Check if the inputs form a valid triangle (sum of any two sides must be greater than the third)
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 'NotATriangle'

    # Check for equilateral triangle (all sides are equal)
    if a == b and b == c:
        return 'Equilateral'

    # Check for right triangle (Pythagorean theorem: a^2 + b^2 = c^2, or any permutation)
    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return 'Right'

    # Check for isosceles triangle (exactly two sides are equal)
    if a == b or b == c or a == c:
        return 'Isosceles'

    # If no sides are equal, it's a scalene triangle
    return 'Scalene'
# new1
