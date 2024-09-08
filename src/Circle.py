from src.Figure import Figure
from math import pi


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Не может быть круга со стороной меньше либо равной 0")
        self.radius = radius

    @property
    def get_area(self):
        return round(pi * self.radius**2, 2)

    @property
    def get_perimetr(self):
        return round(2 * self.radius * pi, 2)
