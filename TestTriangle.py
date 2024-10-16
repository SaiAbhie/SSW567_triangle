# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    
    # Test for right triangles
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6,8,10 is a Right triangle')

    # Test for equilateral triangles
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    # Test for isosceles triangles
    def testIsoscelesTrianglesA(self):
        self.assertEqual(classifyTriangle(5, 5, 8), 'Isosceles', '5,5,8 should be isosceles')

    def testIsoscelesTrianglesB(self):
        self.assertEqual(classifyTriangle(5, 8, 5), 'Isosceles', '5,8,5 should be isosceles')

    def testIsoscelesTrianglesC(self):
        self.assertEqual(classifyTriangle(8, 5, 5), 'Isosceles', '8,5,5 should be isosceles')

    # Test for scalene triangles
    def testScaleneTriangles(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 should be scalene')

    # Test for invalid triangles
    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(0, 4, 5), 'InvalidInput', '0,4,5 should be invalid')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(-1, 4, 5), 'InvalidInput', '-1,4,5 should be invalid')

    def testInvalidTriangleC(self):
        self.assertEqual(classifyTriangle(1, 10, 12), 'NotATriangle', '1,10,12 is not a valid triangle')

    def testInvalidTriangleD(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a valid triangle')

    # Test for float inputs (invalid, because the function expects integers)
    def testFloatInputs(self):
        self.assertEqual(classifyTriangle(3.5, 4.5, 5.5), 'InvalidInput', '3.5,4.5,5.5 should be invalid')

    # Test for string inputs (invalid)
    def testStringInputs(self):
        self.assertEqual(classifyTriangle('a', 'b', 'c'), 'InvalidInput', 'String inputs should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
