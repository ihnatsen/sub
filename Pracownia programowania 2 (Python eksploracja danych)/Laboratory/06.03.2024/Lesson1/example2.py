# 06.03.2024
class Triangle:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def get_sides(self):
        return self.__a, self.__b

    def set_sides(self, a, b):
        self.__a = a
        self.__b = b


triangle = Triangle(5, 10)
triangle.set_sides(6, 11)
print(triangle.get_sides())
