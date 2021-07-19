# стандартные библиотеки python
# функции, область видимости, параметры, параметры по умолчанию, типизация

import string
import random
# import random as rnd

print(string.ascii_lowercase)



value = random.randint(100, 200)
my_list = [1, 2, 3, 10, 20, 30]
# my_list = [True, False]
my_str = 'qwerty'
choice_from_list = random.choice(my_str)
print(value, choice_from_list)
# new_list = random.shuffle(my_list)  # стандартная ошибка!!!
# print(new_list)
new_list = my_list.copy()  # shuffle меняет объект!!! поэтому нужен copy
random.shuffle(new_list)
print(my_list, new_list)



# from random import randint, choice
#
# my_str = 'qwerty'
# choice_from_list = choice(my_str)
# value = randint(100, 200)
# print(value, choice_from_list)


import random

# DRY

point_A = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_B = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_C = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

triangle_ABC = {"A": point_A,
                "B": point_B,
                "C": point_C}

point_M = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_N = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

point_K = {"x": random.randint(-10, 10),
           "y": random.randint(-10, 10)}

triangle_MNK = {"M": point_M,
                "N": point_N,
                "K": point_K}

print(triangle_MNK)




import random


def create_point(min_limit, max_limit):
    point = {"x": random.randint(min_limit, max_limit),
             "y": random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name_str, min_limit, max_limit):
    return {key: create_point(min_limit, max_limit) for key in points_name_str}


triangle_ABC = create_triangle("ABC", -100, 100)
triangle_MNK = create_triangle("MNK", -10, 10)
triangle_QWE = create_triangle("QWE", -5, 23)

print(triangle_ABC)
print(triangle_MNK)
print(triangle_QWE)


import random

MIN_LIMIT = -1
MAX_LIMIT = 1


def create_point(min_limit: int = MIN_LIMIT, max_limit=MAX_LIMIT) -> dict:
    point = {"x": random.randint(min_limit, max_limit),
             "y": random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name_str: str) -> dict:
    return {key: create_point() for key in points_name_str}


def print_triangles_list(triangles_list: list) -> None:
    print("-----------------------------------------------------------------")
    for triangle in triangles_list:
        print(triangle)
    print("-----------------------------------------------------------------")


















triangles_list = []
names = ["ABC", "MNK", "QWE", "ZSD"]
for name in names:
    triangle = create_triangle(name)
    triangles_list.append(triangle)
print_triangles_list(triangles_list)

# triangle_ABC = create_triangle("ABC")
# triangle_MNK = create_triangle("MNK")
# triangle_QWE = create_triangle("QWE")
#
# print(triangle_ABC)
# print(triangle_MNK)
# print(triangle_QWE)


import random

MIN_LIMIT = -1
MAX_LIMIT = 1


def create_point(min_limit: int = MIN_LIMIT, max_limit=MAX_LIMIT) -> dict:
    point = {"x": random.randint(min_limit, max_limit),
             "y": random.randint(min_limit, max_limit)}
    return point


def create_triangle(points_name_str: str) -> dict:
    return {key: create_point() for key in points_name_str}


def print_triangles_list(triangles_list: list) -> None:
    print("-----------------------------------------------------------------")
    for triangle in triangles_list:
        print(triangle)
    print("-----------------------------------------------------------------")






triangles_list = []
names = ["ABC", "MNK", "QWE", "ZSD"]
for name in names:
    triangle = create_triangle(name)
    triangles_list.append(triangle)
print_triangles_list(triangles_list)

# triangle_ABC = create_triangle("ABC")
# triangle_MNK = create_triangle("MNK")
# triangle_QWE = create_triangle("QWE")
#
# print(triangle_ABC)
# print(triangle_MNK)
# print(triangle_QWE)