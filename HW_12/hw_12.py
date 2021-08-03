import json


# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"


def read_data(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
    return data


def get_name(data):
    name = data.get('name').split(' ')
    if len(name) == 1:
        return name[0]
    else:
        return name[-1]


def get_text_len(data):
    text_len = len(data.get('text'))
    return text_len


def sort_by_name(data):
    return sorted(data, key=get_name)


def sort_by_len(data):
    return sorted(data, key=get_text_len)


print(sort_by_name(read_data("data.json")))
print(sort_by_len(read_data("data.json")))
