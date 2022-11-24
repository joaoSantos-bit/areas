
# importing needed libraries
import math

class areas:
    
    def calculateCircleArea(radius):
        return math.pow(radius, 2) * math.pi

    def calculateSquareArea(side):
        return math.pow(side, 2)

    def calculateTriangleArea(base, height):
        return (base * height) / 2

    def calculateRectangleArea(base, height):
        return base * height

    def calculateDiamondArea(d1, d1):
        return (d1 * d2) / 2