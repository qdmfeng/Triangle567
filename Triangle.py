# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""
import math


def classify_triangle(a, b, c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'

      BEWARE: there may be a bug or two in this code
    """
    ret = ""
    a, b, c = sorted([a, b, c])
    if not ((a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    # now we know that we have a valid triangle
    if math.isclose((a ** 2) + (b ** 2), (c ** 2), rel_tol=1e-2):
        ret += 'Right '
    if a == b and b == a and c == a:
        ret += 'Equilateral'
    elif (a != b) and (b != c) and (a != c):
        ret += 'Scalene'
    else:
        ret += 'Isosceles'
    return ret
