import pytest
from src.circle import Circle


@pytest.mark.smoke
@pytest.mark.parametrize(
    "radius, area",
    [
        (3, 28.27),
        (3.5, 38.48),
    ],
    ids=["integer", "float"],
)
def test_circle_area_positive(check_circle, radius, area):
    c = Circle(radius)
    assert c.area == area, f"Площадь должна быть равна {area}]"


@pytest.mark.parametrize(
    "radius, perimetr",
    [
        (10, 62.83),
        (12.25, 76.97),
    ],
    ids=["integer", "float"],
)
def test_circle_perimetr_positive(check_circle, radius, perimetr):
    c = Circle(radius)
    assert c.perimetr == perimetr, f"Периметр должен быть равен {perimetr}]"
