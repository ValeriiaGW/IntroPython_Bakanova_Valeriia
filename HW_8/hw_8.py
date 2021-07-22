# 1) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена самых молодых.
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
# в) Посчитать среднее количество лет всех людей из списка.
#
# 2) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
#
# {1:1, 2:2}, {11:11, 2:22} ---> {1:1, 11:11, 2:[2, 22]}


persons = [
    {"name": "Johon", "age": 15},
    {"name": "Mike", "age": 35},
    {"name": "Anna", "age": 15},
    {"name": "Sara", "age": 75},
    {"name": "Jack", "age": 45},
]




min_age = persons[0].get("age")
#
for person in persons:
    age = person.get("age")
    if age < min_age:
        min_age = age

for person in persons:
    if min_age == person.get('age'):
        print(person.get('name'))

#
long_name = len(persons[0].get('name'))

for person in persons:
    if len(person.get("name")) > long_name:
        long_name = len(person.get("name"))

for person in persons:
    if len(person.get("name")) == long_name:
        print(person.get('name'))



print('\n Task 1c')
sum_age = 0

for person in persons:
    sum_age += person.get('age')

print(sum_age / len(persons))
#
####################################

# from functools import reduce
#
# total_age = 0
# for person in persons:
#     total_age += person.get("age")
#
# total_age = reduce(lambda x, p: x + p.get("age"), persons, 0)
# print(total_age)
####################################


# my_dict1 = {1: 1, 2: 2}
# my_dict2 = {2: 3, 3: 4}
#
# new_dict = my_dict1.copy()
# for key, value in my_dict2.items():
#     if key in new_dict:
#         new_dict[key] = [new_dict[key], value]
#     else:
#         new_dict[key] = value
#
# print(new_dict)

