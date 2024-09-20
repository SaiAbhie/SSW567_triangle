def classify_triangle(side1, side2, side3):
    """
    Classifies the type of triangle based on side lengths side1, side2, and side3.

    Parameters:
        side1 (float): The length of side 1.
        side2 (float): The length of side 2.
        side3 (float): The length of side 3.
    Returns:
        str: A string specifying the type of triangle.
    """
    
    # Ensure inputs are valid
    if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
        return "Invalid triangle"

    # Equilateral Triangle
    if side1 == side2 == side3:
        return "Equilateral"
    
    # Isosceles Triangle
    elif side1 == side2 or side2 == side3 or side1 == side3:
        if round(side1**2 + side2**2, 5) == round(side3**2, 5) or \
           round(side2**2 + side3**2, 5) == round(side1**2, 5) or \
           round(side1**2 + side3**2, 5) == round(side2**2, 5):
            return "Isosceles and Right Triangle"
        return "Isosceles"
    
    # Scalene Triangle
    else:
        if round(side1**2 + side2**2, 5) == round(side3**2, 5) or \
           round(side2**2 + side3**2, 5) == round(side1**2, 5) or \
           round(side1**2 + side3**2, 5) == round(side2**2, 5):
            return "Scalene and Right Triangle"
        return "Scalene"


def main():
    """
    Main function that takes user input and classifies the triangle.
    """
    print("Please enter the lengths of the three sides of your triangle:")
    side1 = float(input("Length of side 1: "))
    side2 = float(input("Length of side 2: "))
    side3 = float(input("Length of side 3: "))
    
    # Call the classify_triangle function
    triangle_type = classify_triangle(side1, side2, side3)
    
    # Print the result
    print(f"The triangle is classified as: {triangle_type}")

# Run the main function
if __name__ == "__main__":
    main()
