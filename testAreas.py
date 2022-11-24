
# importing libraries
import unittest
from areas import Areas

class TestAreas(unittest.TestCase):

    def testSquareArea(self):
        self.assertAlmostEqual(400.0, Formas.areaQuadrado(20), 1)
        self.assertAlmostEqual(225.0, Formas.areaQuadrado(15), 1)

    def testTriangleArea(self):
        self.assertAlmostEqual(75.0, Formas.areaTriangulo(15, 10), 1)
        self.assertAlmostEqual(350.0, Formas.areaTriangulo(350, 2), 1)

    def testCircleArea(self):
        self.assertAlmostEqual(907.92, Formas.volumeTetraedro(17), 1)
        self.assertAlmostEqual(254.46, Formas.volumeTetraedro(9), 1)

    def testDiamondArea(self):
        self.assertAlmostEqual(100.0, Formas.volumeTetraedro(10, 20), 1)
        self.assertAlmostEqual(27.0, Formas.volumeTetraedro(9, 6), 1)

    def testRectangleArea(self):
        self.assertAlmostEqual(300.0, Formas.areaRetangulo(10, 30), 1)
        self.assertAlmostEqual(16.0, Formas.areaRetangulo(576, 72), 1)