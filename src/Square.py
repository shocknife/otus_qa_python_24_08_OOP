from src.Rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Не может быть квадрата со стороной меньше либо равной 0")
        super().__init__(side_a, side_a)
        self.side_a = side_a
