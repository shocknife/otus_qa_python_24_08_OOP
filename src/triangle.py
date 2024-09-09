from src.figure import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not (
            side_a + side_b > side_c
            and side_a + side_c > side_b
            and side_b + side_c > side_a
        ) or (side_a < 0 and side_b < 0 and side_c < 0):
            raise ValueError("Треугольника не существует")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def area(self):
        p = (self.get_perimetr) / 2
        return round(
            sqrt(p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 3
        )

    @property
    def perimetr(self):
        return self.side_a + self.side_b + self.side_c
