import random
import string



# Для задания 1-7 за основу можете взять код из ДЗ № 6.
#
# 1. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.


my_list = ["один", "два", "три", "четыре", "пять", "шесть"]


def create_first_list(my_list):
    new_list = []
    for i in range(len(my_list)):
        if not i % 2:
            new_list.append(my_list[i][::-1])
        else:
            new_list.append(my_list[i])
    return new_list


print(f'Task 1 = {create_first_list(my_list)}')


# 2. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list у которых первый символ - буква "a".

my_list_2 = ["aerty", "dfgh", "dfghj", "awert", "aert"]


def create_second_list(my_list_2):
    new_list = []
    for element in my_list_2:
        if element[0] == "a":
            new_list.append(element)
    return new_list


print(f'Task 2 = {create_second_list(my_list_2)}')


# 3. Написать функцию которой передается один параметр - список строк my_list.
# Функция возвращает новый список в котором содержаться
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list_3 = ["aerty", "dfagh", "dfghj", "wert", "erta"]


def create_third_list(my_list_3):
    new_list = []
    for element in my_list_3:
        if "a" in element:
            new_list.append(element)
    return new_list


print(f'Task 3 = {create_third_list(my_list_3)}')

# 4. Написать функцию которой передается один параметр - список строк my_list в
# котором могут быть как строки (type str) так и целые числа (type int).
# Функция возвращает новый список в котором содержаться только строки из my_list.

my_list_4 = [1, 2, 3, "11", "22", 33, "juhi"]


def create_forth_list(my_list_4):
    new_list = []
    for element in my_list_4:
        if type(element) == str:
            new_list.append(element)
    return new_list


print(f'Task 4 = {create_forth_list(my_list_4)}')

# 5. Написать функцию которой передается один параметр - строка my_str.
# Функция возвращает новый список в котором содержаться те символы из my_str,
# которые встречаются в строке только один раз.

my_str = "qweewewqeqwwewerwqqqq"


def create_fifth_list(my_str):
    new_list = []

    for symbol in my_str:
        count_symbol = my_str.count(symbol)

        if count_symbol == 1:
            new_list.append(symbol)

    return new_list


print(f'Task 5 = {create_fifth_list(my_str)}')


# 6. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "qweewewqeqwwewerwqqqq"
my_str_2 = "qweefkllkewjblvjqwwfjnvlewqq"


def create_sixth_list(my_str_1: str, my_str_2):
    my_set_1 = set(my_str_1)
    my_set_2 = set(my_str_2)
    intersection_of_sets = list(my_set_1.intersection(my_set_2))
    return intersection_of_sets


print(f'Task 6 = {create_sixth_list(my_str_1, my_str_2)}')

# 7. Написать функцию которой передается два параметра - две строки.
# Функция возвращает список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
#
my_str_1 = "zqweewewq8eqwweywerwqqqq"
my_str_2 = "qzweefkllkewjbly8vjqwwfjnvlewqq"


def create_seventh_list(my_str_1, my_str_2):
    my_list = []
    my_set_1 = set(my_str_1)
    my_set_2 = set(my_str_2)
    intersection_of_sets = list(my_set_1.intersection(my_set_2))

    for element in intersection_of_sets:
        if my_str_1.count(element) == 1 and my_str_2.count(element) == 1:
            my_list.append(element)

    return my_list


print(f'Task 7 = {create_seventh_list(my_str_1, my_str_2)}')

# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]


def create_email():
    name = random.choice(names)
    domain = random.choice(domains)
    number = random.randint(100, 999)

    letters = string.ascii_uppercase
    my_str = ''.join(random.choice(letters) for letter in range(random.randint(5, 7)))

    email = name + str(number) + "@" + my_str + "." + domain

    return email


print(create_email())