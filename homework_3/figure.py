import math


class Figure:
    _figure_name = None
    _angles = None

    def __init__(self, a=None, b=None, c=None, r=None):
        self._a = a
        self._b = b
        self._c = c
        self._r = r
        self.__figure_name = self._figure_name
        self.__angles = self._angles

    def name(self):
        return self._figure_name

    def angles(self):
        return self._angles

    def area(self):
        if self.__class__ == Rectangle:
            return round(self._a * self._b, 2)
        elif self.__class__ == Square:
            return round(self._a ** 2, 2)
        elif self.__class__ == Triangle:
            return round(self._a + self._b + self._c)
        elif self.__class__ == Circle:
            return round(math.pi * self._r ** 2, 2)

    def perimeter(self):
        if self.__class__ == Square:
            return round(self._a * 4, 2)
        elif self.__class__ == Rectangle:
            return round((self._a + self._b) * 2, 2)
        elif self.__class__ == Circle:
            return round(2 * math.pi * self._r, 2)
        elif self.__class__ == Triangle:
            return round(self._a + self._b + self._c, 2)

    # TODO: не работает, необходимо подумать
    def add_square_area(self, other_figure):
        return self.area + other_figure.area()


class Rectangle(Figure):
    _angles = 4
    _figure_name = 'Rectangle'

    def __init__(self, a, b):
        super().__init__(a, b)
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles


class Square(Figure):
    _angles = 4
    _figure_name = 'Square'

    def __init__(self, a):
        super().__init__(a)
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles


class Circle(Figure):
    _angles = 0
    _figure_name = 'Circle'

    def __init__(self, r):
        super().__init__(r)
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
        self._r = r


class Triangle(Figure):
    _angles = 3
    _figure_name = 'Triangle'

    def __init__(self, a, b, c):
        super().__init__(a, b, c)
        self.__figure_name = self._figure_name
        self.__angles_number = self._angles
