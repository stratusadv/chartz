from abc import ABC, abstractmethod


class TrendLine(ABC):
    def __init__(self, data: list[float]):
        self.y_values = data
        self.x_values = list(range(1, len(data) + 1))

    @abstractmethod
    def generate(self) -> list[float]:
        pass


class LeastSquaresTrendLine(TrendLine):
    """
        The least squares method is widely used for linear regression because it provides an optimal solution to
        estimate the relationship between variables in a linear manner.
        It is a simple, effective, and computationally efficient method for fitting a line to a set of data points.
    """

    def __init__(self, data: list[float]):
        super().__init__(data)
        self.clean_data()
        self._x_mean = sum(self.x_values) / len(self.x_values)
        self._y_mean = sum(self.y_values) / len(self.y_values)

    def clean_data(self) -> None:
        self.y_values = [float(value) for value in self.y_values]

    @property
    def x_mean(self) -> float:
        return self._x_mean

    @property
    def y_mean(self) -> float:
        return self._y_mean

    def slope(self) -> float:
        """
            slope = Σ((x - x_mean) * (y - y_mean)) / Σ((x - x_mean)²)
        """
        x_mean = self.x_mean
        y_mean = self.y_mean

        numerator = 0
        denominator = 0

        for (x, y) in zip(self.x_values, self.y_values):
            numerator += (x - x_mean) * (y - y_mean)
            denominator += (x - x_mean) ** 2

        return numerator / denominator

    def intercept(self) -> float:
        """
            b = y - mx
        """
        return self.y_mean - (self.slope() * self.x_mean)

    def generate(self) -> list[float]:
        """
            y = mx + b
        """
        return [self.slope() * x + self.intercept() for x in self.x_values]
