# # функции сортировки
#
# # my_list = [12, 3, 45, 23, -10, 1]
# # sorted_list = sorted(my_list, reverse=True)
# # print(sorted_list)
# #
# # my_str_list = ["John", "Jack", "Jacob", "Max", "Violeta"]
# # sort_str_list = sorted(my_str_list)  # сортировка по алфавиту
# # print(sort_str_list)
# #
# # sort_str_list = sorted(my_str_list, key=len)  # по длине
# # print(sort_str_list)
# #
# #
# # my_list = [12, 3, 45, 23, -10, 1]
# # sorted_list = sorted(my_list, key=abs)  # key=abs - сортировка по модулю
# # print(sorted_list)
#
# ######### осртировка словарей
#
# # сортировка по цене
#
# def sort_by_price(price_dict):
#     price = price_dict["price"]
#     return price
# price_list = [{"product": "milk", "price": 23},
#               {"product": "ice-cream", "price": 18},
#               {"product": "meat", "price": 120},
#               {"product": "coca-cola", "price": 10}]
# sorted_price_list = sorted(price_list, key=sort_by_price)
# print(sorted_price_list)
#
# ##########################
#
# ## сортировка по цене и имени
# # def sort_by_price(price_dict):
# #     price = price_dict["price"]
# #     name = price_dict["product"]
# #     return price, name
# #
# #
# # price_list = [{"product": "milk", "price": 23},
# #               {"product": "ice-cream", "price": 18},
# #               {"product": "meat", "price": 120},
# #               {"product": "pepsi-cola", "price": 10},
# #               {"product": "coca-cola", "price": 10}]
# #
# # sorted_price_list = sorted(price_list, key=sort_by_price)
# # print(sorted_price_list)
#
# ######
# ## сортировка по длине, но если длина совпадает - по алфавиту
#
#
# # def sort_by_len_and_name(name):
# #
# #
# #     return len(name), name
# #
# #
# # my_str_list = ["John", "Jack", "Jacob", "Max", "Violeta"]
# #
# # sort_str_list = sorted(my_str_list, key=sort_by_len_and_name)
# # print(sort_str_list)
#
#
# ## регулярные выражения
#
# import re
#
#
# my_string = "lljabhbhdvbjfjlkl,sda 127.0.0.1 sjbbklknkjb,z h   uhbdjhbj jij b 200.23.12.201:5400 jdbj bjb"
#
# # template = r'\d+' # d - это digit, d+ - хотя бы 1 цифру, d{1} - только одну цифру, d{1,3} - группа из 1-3х символов (диапазон)
# template = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
# result = re.findall(template, my_string)
# print(result)
#
#
# # числовые группы могут быть записаны r'[0-9a-zA-ZA-Я]+'  любой символ из данных
#
#
#
#
import random
import string


def generate_string(min_limit=50, max_limit=100):
    len_str = random.randint(min_limit, max_limit)
    res_str = "".join([random.choice(string.ascii_lowercase) for _ in range(len_str)])
    return res_str


def choice_transform(word):
    word = word.capitalize()
    return word
def transform_str_by_words(some_str):
    new_words = []
    words = some_str.split()
    for word in words:
        word = choice_transform(word)
        new_words.append(word)
    return " ".join(new_words)

def insert_spaces(some_str):
    go_jump = True
    total_index = 0
    some_list = list(some_str)
    while go_jump:
        jump_index = random.randint(2, 11)
        current_index = total_index + jump_index
        if current_index < len(some_list):
            some_list[current_index] = " "
            total_index += jump_index
        else:
            go_jump = False

    return "".join(some_list)

def transform_str(some_str):
    some_str = insert_spaces(some_str)
    some_str = transform_str_by_words(some_str)
    return some_str


rand_str = generate_string()
tr_str = transform_str(rand_str)
print(tr_str)