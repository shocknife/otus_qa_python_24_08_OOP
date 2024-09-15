import pytest


@pytest.fixture(scope="session", autouse=True)
def check_figures():
    print("\n Запуск проверок фигур")

    yield

    print("\n Окончание проверок фигур")


@pytest.fixture()
def check_circle():
    print("\n Начало проверки круга")

    yield

    print("\n Конец проверки круга")


@pytest.fixture(scope="session")
def check_rectangle():
    print("\n Начало проверки прямоугольника")

    yield

    print("\n Конец проверки прямоугольника")


@pytest.fixture(scope="module")
def check_square(check_rectangle):
    print("\n Начало проверки квадрата (частный случай прямоугольника)")
    print("\n Загрузка данных из API")
    side_a, area = 5, 25
    yield side_a, area

    print("\n Конец проверки квадрата (частный случай прямоугольника)")


@pytest.fixture()
def check_triangle():
    print("\n Начало проверки треугольника")

    yield

    print("\n Конец проверки треугольника")
