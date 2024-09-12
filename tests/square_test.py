import pytest
from src.square import Square


@pytest.mark.posit
def test_square_area_positive(check_square):
    side_a, area = check_square
    s = Square(side_a)
    assert s.area == area, f"Площадь должна быть равна {area}]"


@pytest.mark.posit
@pytest.mark.parametrize(
    "side_a, perimetr",
    [
        (10, 40),
        (1.25, 5.00),
    ],
    ids=["integer", "float"],
)
def test_square_perimetr_positive(check_square, side_a, perimetr):
    s = Square(side_a)
    assert s.perimetr == perimetr, f"Периметр должен быть равен {perimetr}]"
