from src.figure import Figure


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(
                "Не может быть прямоугольника со стороной меньше либо равной 0"
            )
        self.side_a = side_a
        self.side_b = side_b

    @property
    def area(self):
        return self.side_a * self.side_b

    @property
    def perimetr(self):
        return (self.side_a + self.side_b) * 2
