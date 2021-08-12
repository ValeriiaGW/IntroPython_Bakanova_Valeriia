import time

# полиморфизм
# магические методы

class Bbox:
    def __init__(self, x0, y0, x1, y1):
        self._x0 = x0
        self._x1 = x1
        self._y0 = y0
        self._y1 = y1

    def __repr__(self):
        return f"(({self._x0}, {self._y0}), ({self._y1}, {self._x1}))"

    def __add__(self, other):
        x0 = self._x0
        y0 = self._y0
        x1 = other._x1
        y1 = other._y1
        return Bbox(x0, y0, x1, y1)

bbox_1 = Bbox(1, 1, 3, 3)
bbox_2 = Bbox(10, 10, 13, 13)

bbox_3 = bbox_1 + bbox_2  # def __add__(self, other)

print(bbox_1)
print(bbox_3)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    @property
    def y(self):
        return self._y

    def distance(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    @staticmethod
    def distance_2_points(x0, y0, x1, y1):
        return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

point = Point(3, 4)
print(point.x, point.y)
print(point.distance())
print(point.distance_2_points(1, 1, 2, 2))




## декораторы



# def time_decorator(some_function):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = some_function(*args, **kwargs)
#         print(time.time() - start_time)
#         return result
#
#     return wrapper
#
#
# @time_decorator
# def factor(number):
#     res = 1
#     for numb in range(1, number):
#         res *= numb
#     return res
#
#
# number = 100
# # start_time = time.time()
# result = factor(number)
# # print(time.time() - start_time)
# print(result)