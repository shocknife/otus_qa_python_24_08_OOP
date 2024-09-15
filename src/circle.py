from src.figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Не может быть круга со радиусом меньше либо равной 0")
        self.radius = radius

    @property
    def area(self):
        return round(pi * self.radius**2, 2)

    @property
    def perimetr(self):
        return round(2 * self.radius * pi, 2)
