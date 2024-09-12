from src.circle import Circle
from src.rectangle import Rectangle
from src.square import Square
from src.triangle import Triangle


def test_summ_add_area_square():
    r = Rectangle(3, 5)
    s = Square(5)
    assert (
        r.add_area(s) == 40
    ), "Сумма площадей Rectangle и Square должна быть равна 40"


def test_summ_add_area_rectangle():
    c = Circle(3)
    r = Rectangle(5, 10)
    assert (
        c.add_area(r) == 78.27
    ), "Сумма площадей Circle и Rectangle должна быть равна 78.27"


def test_summ_add_area_triangle():
    s = Square(3)
    t = Triangle(10, 11, 12)
    assert (
        s.add_area(t) == 60.52
    ), "Сумма площадей Square и Triangle должна быть равна 60.52"
