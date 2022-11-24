
# importing libraries
import unittest
from areas import Areas

class TestAreas(unittest.TestCase):

    def testSquareArea(self):
        self.assertAlmostEqual(400.0, Areas.calculateSquareArea(20), 1)
        self.assertAlmostEqual(225.0, Areas.calculateSquareArea(15), 1)

    def testTriangleArea(self):
        self.assertAlmostEqual(75.0, Areas.calculateTriangleArea(15, 10), 1)
        self.assertAlmostEqual(350.0, Areas.calculateTriangleArea(350, 2), 1)

    def testCircleArea(self):
        self.assertAlmostEqual(907.92, Areas.calculateCircleArea(17), 1)
        self.assertAlmostEqual(254.46, Areas.calculateCircleArea(9), 1)

    def testDiamondArea(self):
        self.assertAlmostEqual(100.0, Areas.calculateDiamondArea(10, 20), 1)
        self.assertAlmostEqual(27.0, Areas.calculateDiamondArea(9, 6), 1)

    def testRectangleArea(self):
        self.assertAlmostEqual(300.0, Areas.calculateRectangleArea(10, 30), 1)
        self.assertAlmostEqual(41472.0, Areas.calculateRectangleArea(576, 72), 1)
