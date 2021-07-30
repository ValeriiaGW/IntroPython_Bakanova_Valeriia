import datetime
import pprint

# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая получает в виде параметра имя файла названия интернет доменов (domains.txt)
# и возвращает их в виде списка строк (названия возвращать без точки).
from typing import List


def get_domains_names(filename):

    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    return data


filename = "domains.txt"
new_list = get_domains_names(filename)
domain_list = [element[1:-1] for element in new_list]
print(domain_list)


# 2. Написать функцию, которая получает в виде параметра имя файла (names.txt)
# и возвращает список всех фамилий из него.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Разделитель - символ табуляции "\t"

filename_2 = "names.txt"
names = []


def get_data(filename_2):
    with open(filename_2) as txt_file:
        data = txt_file.readlines()
    return data


def create_list_of_persons(data):
    names = []
    names_list = [element.split("\t") for element in data]
    for person in names_list:
        names.append(person[1])
    return names


print(create_list_of_persons(get_data(filename_2)))



# 3. Написать функцию, которая получает в виде параметра имя файла (authors.txt) и возвращает список
# словарей вида {"date_original": date_original, "date_modified": date_modified}
# в которых date_original - это дата из строки (если есть),
# а date_modified - эта же дата, представленная в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"date_original": "8th February 1828", "date_modified": 08/02/1828},  ...]

filename_3 = "authors.txt"


def read_file(filename_3):
    with open(filename_3) as txt_file:
        data = txt_file.readlines()
    return data


def format_date(data: list) -> list:
    dates = []
    for element in data:
        elements = element.split(' ')
        elements[0] = elements[0][0:-2]
        date_str = ' '.join(elements)
        try:
            date = datetime.datetime.strptime(date_str, "%d %B %Y").date()
        except:
            pass
        else:
            dates.append({
                'date_original': element,
                'date_modified': datetime.datetime.strftime(date, "%d/%m/%Y")
            })

    return dates


def process_data(data: list) -> list:
    split_list = []
    for line in data:
        items = line.split(" - ")
        dates = format_date(items)
        split_list.extend(dates)
    return split_list


print(process_data(read_file(filename_3)))
