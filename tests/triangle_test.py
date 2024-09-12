import pytest
from src.triangle import Triangle


@pytest.mark.posit
@pytest.mark.parametrize(
    "side_a, side_b, side_c, area",
    [
        (10, 15, 12, 59.81),
        pytest.param(10.5, 15.9, 12.5, 65.54, marks=pytest.mark.smoke),
    ],
    ids=["integer", "float"],
)
def test_triangle_area_positive(check_triangle, side_a, side_b, side_c, area):
    t = Triangle(side_a, side_b, side_c)
    assert t.area == area, f"Площадь должна быть равна {area}]"


@pytest.mark.posit
@pytest.mark.parametrize(
    "side_a, side_b, side_c, perimetr",
    [
        (11, 12, 13, 36),
        (10.5, 10.6, 11.3, 32.4),
    ],
    ids=["integer", "float"],
)
def test_triangle_perimetr_positive(check_triangle, side_a, side_b, side_c, perimetr):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimetr == perimetr, f"Периметр должен быть равен {perimetr}]"


@pytest.mark.parametrize(
    "side_a, side_b, side_c",
    [(0, 10, 12), (4, 0, 7), (4, 5, 0)],
    ids=["check side A", "check side B", "check side C"],
)
@pytest.mark.neg
def test_triangle_negative_side(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)
