import json


# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"


filename = "data.json"


def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    return data

#
# # print(read_data("data.json"))
#
# def get_names(data):
#     # names = data.get("name").split(" ")
#     # return [name[-1] for name in names]
#
#     full_names = [dictionary.get("name") for dictionary in data]
#     name = [name[-1] for name in [name.split() for name in full_names]]
#     return name
#
#
# print(sorted(read_data("data.json"), key=get_names))


# def sort_name(data):
#     sorted_list = sorted(read_data("data.json"), key=get_names)
#     return sorted_list
# #
# #
# print(sort_name(get_names(read_data("data.json"))))



# def sort_by_text_len(data):
#     return len(data['text'])
#
#
def get_name(data):
    name = data.get('name').split(' ')
    if len(name) == 1:
        return name[0]
    else:
        return name[-1]


def sort_by_name(data):
    return sorted(data, key=get_name)
# print(sorted(data, key=sort_by_text_len))

print(sort_by_name(read_data("data.json")))
