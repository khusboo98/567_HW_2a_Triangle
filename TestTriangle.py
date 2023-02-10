# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
    
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be equilateral')
        
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(2,1,1),'Isoceles','2,1,1 should be isoceles')    

    def testIsocelesTriangleB(self): 
        self.assertEqual(classifyTriangle(1,2,1),'Isoceles','1,2,1 should be isoceles')

    def testScaleneTrianglesA(self): 
        self.assertEqual(classifyTriangle(2,3,1),'Scalene','2,3,1 should be scalene') 
    
    def testScaleneTrianglesB(self): 
        self.assertEqual(classifyTriangle(2,5,6),'Scalene','2,5,6 should be scalene') 

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(202,1,1),'InvalidInput','202,1,1 should be invalid')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1,2,1),'InvalidInput','-1,2,1 should be invalid')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(1.5,3,2),'InvalidInput','1.5,3,2 should be invalid')
    
    def testInvalidInputD(self):
        self.assertEqual(classifyTriangle(0,0,0),'InvalidInput','0,0,0 should be invalid')

    def testInvalidInputE(self):
        self.assertEqual(classifyTriangle(1,2,15),'NotATriangle','1,2,15 should not be a triangle')  

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

