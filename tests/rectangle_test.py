import pytest
from src.rectangle import Rectangle


@pytest.mark.parametrize(
    "side_a, side_b, area",
    [
        (3, 5, 15),
        pytest.param(3.5, 5.5, 19.25, marks=pytest.mark.skip("На float заведен баг ")),
    ],
    ids=["integer", "float"],
)
def test_rectangle_area_positive(check_rectangle, side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f"Площадь должна быть равна {area}]"


@pytest.mark.parametrize(
    "side_a, side_b, perimetr",
    [
        (10, 15, 50),
        (1.25, 2.5, 7.5),
    ],
    ids=["integer", "float"],
)
def test_rectangle_perimetr_positive(check_rectangle, side_a, side_b, perimetr):
    r = Rectangle(side_a, side_b)
    assert r.perimetr == perimetr, f"Периметр должен быть равен {perimetr}]"
