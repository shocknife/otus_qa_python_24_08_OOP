from abc import ABC, abstractmethod


class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimetr(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError(f"Аргумент {figure} должен быть объектом класса Figure")
        return self.area + figure.area
