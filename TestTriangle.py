# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
import math

from triangle import classify_triangle as classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right Scalene', '3,4,5 is a Right Scalene triangle')

    def testRightScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right Scalene', '5,3,4 is a Right Scalene triangle')

    def testRightIsocelesA(self):
        self.assertEqual("Right Isosceles", classifyTriangle(1, 1, math.sqrt(2)))

    def testRightIsocelesB(self):
        self.assertEqual("Right Isosceles", classifyTriangle(math.sqrt(2), 2, math.sqrt(2)))

    def testEquilateralTrianglesA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTrianglesB(self):
        self.assertEqual(classifyTriangle(7, 7, 7), 'Equilateral', '7,7,7 should be equilateral')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(14, 14, 17), 'Isosceles', '14,14,17 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(14, 17, 14), 'Isosceles', '14,17,14 is an Isosceles triangle')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(22, 16, 18), 'Scalene', '22,16,18 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(12, 16, 17), 'Scalene', '12,16,17 is a Scalene triangle')

    def testScaleneTriangleC(self):
        self.assertEqual(classifyTriangle(9, 6, 4), 'Scalene', '9,6,4 is a Scalene triangle')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle('x', '7', 'z'), 'InvalidInput', 'x,7,z is an Invalid input')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(200, 777, 121), 'InvalidInput', '200,777,121 is an Invalid input')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(42, 11, -17), 'InvalidInput', '42,11,-17 is an Invalid input')

    def testNotTriangleA(self):
        self.assertEqual(classifyTriangle(4, 17, 2), 'NotATriangle', '4,17,2 is not a triangle')

    def testNotTriangleB(self):
        self.assertEqual(classifyTriangle(7, 3, 3), 'NotATriangle', '7,3,3 is not a triangle')

    def testNotTriangleC(self):
        self.assertEqual(classifyTriangle(20, 14, 1), 'NotATriangle', '20,14,1 is not a triangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
