# генератор списка
# множества set  -  не сохраняет порядок
##### - intersection - совпадения
##### - union - обобщение, все значения
##### - difference - то что есть у одного и  нет у другого


# словарь - dict не гарантирует порядок, все ключи уникальны
#### ключи - любые неизменяемые объекты (строка, кортеж, число)

triangle = {"A": {"x": 1, "y": 2},
            "B": {"x": 3, "y": 4},
            "C": {"x": 5, "y": 6}}
print(triangle["B"]["y"])


#########################################################################################
# Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и
# my_list_2 через один, начиная с my_list_1.
# a) кол-во эл-тов одинаковое
# б) кол-во эл-тов разное. Оставшиеся дописать в конец.

my_list_1 = [1, 2, 3, 4, ]
my_list_2 = [10, 20, 30, 40, 50]
my_result = []

min_len_lists = min(len(my_list_1), len(my_list_2))

for index in range(min_len_lists):
    my_result.append(my_list_1[index])
    my_result.append(my_list_2[index])

last_values_list_1 = my_list_1[min_len_lists:]
last_values_list_2 = my_list_2[min_len_lists:]

my_result = my_result + last_values_list_1 + last_values_list_2

print(my_result)

# id() - номер объекта в памяти
my_list = [1, 2, 3]
print(id(my_list))
my_list = [2, 3, 4, 5]
print(id(my_list))
my_list.append(6)
print(id(my_list))

my_list = [1, 2, 3]

result = []
print(id(result))

result = result + my_list
print(id(result))

result += my_list
print(id(result))

value = 10
value += 2
print(value)

value = 10
value = value + 2
print(value)

# генератор списков
folders = []
for digit in range(1, 21):
    folder = f"/tpm/{digit}"
    folders.append(folder)
print(folders)

folders = [f"/tpm/{digit}" for digit in range(1, 21) if not digit % 3]
print(folders)

symbols = [ord(symbol) for symbol in 'eyuioa']
print(symbols)

alphabet = [chr(ord_index) for ord_index in range(ord("a"), ord("z") + 1)]
alphabet = "".join(alphabet)
print(alphabet)

#################################################
# множества set - не сохраняет порядок, все элементы уникальные

my_list = [3, 10, 10, 2, "2", 2, 3, 3, 3, 3, 3, 3, 3]
# my_list_unique = list(set(my_list)) - убирает дубли
my_set = set(my_list)
print(my_set)
my_list_unique = list(my_set)
print(my_list_unique)

new_set = {1, 2, 3, 54, 54, 54}
print(new_set)

# см. lesson5 3)
my_str = "bla BLA car"
my_str = my_str.lower()
res_len = len(set(my_str))
print(res_len)

my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqwweeeeeeeeeeeeeeeerty"
for symbol in set(my_str):
    print(symbol, my_str.count(symbol))

my_str_1 = "qwerty1234567890"
my_str_2 = "qweasd123456789"

my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)

intersection = my_set_1.intersection(my_set_2)
print(intersection)
union = my_set_1.union(my_set_2)
print(union)
difference = my_set_2.difference(my_set_1)
print(difference)

# словарь - dict  не гарантирует порядок, все ключи уникальные, остается последнее значение
# ключи - любые неизменяемые объекты
# значения - любые объекты

triangle = [[1, 1], [2, 3], [4, -2]]
print(triangle[1][1])
key = (1,2,"qwe")
test_dict = {11: "qwerty",
             "11": 12,
              key: 'test'}
print(test_dict[key])

triangle = {"A": {"x": 1, "y": 1},
            "B": {"x": 2, "y": 3},
            "С": {"x": 4, "y": -2}}

print(triangle["B"]["y"])
print(triangle)