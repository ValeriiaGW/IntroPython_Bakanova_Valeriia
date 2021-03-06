# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
#

persons = [
    {"name": "Jon", "age": 15},
    {"name": "Mike", "age": 35},
    {"name": "Anna", "age": 15},
    {"name": "Samanta", "age": 75},
    {"name": "Jack", "age": 45},
]

age_list = []
names_length = []

for person in persons:

    age = person.get("age")
    age_list.append(age)
    long_name = len(person.get("name"))
    names_length.append(long_name)

min_age = min(age_list)

for person in persons:
    if person.get("age") == min_age:
        print(person.get("name"))

max_name_length = max(names_length)

for person in persons:
    if len(person.get("name")) == max_name_length:
        print(person.get("name"))


avg_age = sum(age_list) / len(age_list)
print(avg_age)


# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}


my_dict1 = {"key1": 1, "key2": 2, "key5": 5}
my_dict2 = {"key1": 1, "key3": 3, "key4": 4}

keys_1 = set(my_dict1.keys())
keys_2 = set(my_dict2.keys())

my_list_a = list(keys_1.intersection(keys_2))

my_list_b = list(keys_1.difference(keys_2))

new_dict_c = {}
for key, value in my_dict1.items():
    if key in my_list_b:
        new_dict_c[key] = value

new_dict_g = my_dict1.copy()
for key, value in my_dict2.items():
    if key in new_dict_g:
        new_dict_g[key] = [new_dict_g[key], value]
    else:
        new_dict_g[key] = value



