# # 1. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list по следующему правилу:
# # Если строка стоит на нечетном месте в my_list, то ее заменить на
# # перевернутую строку. "qwe" на "ewq".
# # Если на четном - оставить без изменения.
# # Задание сделать с использованием enumerate или range.



my_list = ["один", "два", "три", "четыре", "пять", "шесть"]
new_list = []

for string in range(len(my_list)):
    if not string % 2:
        new_list.append(my_list[string][::-1])
    else:
        new_list.append(my_list[string])
print(new_list)




# # 2. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list у которых первый символ - буква "a".



my_list = ["aerty", "dfgh", "dfghj", "awert", "aert"]
new_list = []

for element in my_list:
    if element[0] == "a":
        new_list.append(element)
print(new_list)



# # 3. Дан список строк my_list. Создать новый список в который поместить
# # элементы из my_list в которых есть символ - буква "a" на любом месте.



my_list = ["aerty", "dfagh", "dfghj", "wert", "erta"]
new_list = []

for element in my_list:
    if "a" in element:
        new_list.append(element)
print(new_list)



# # 4. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# # Например [1, 2, 3, "11", "22", 33]
# # Создать новый список в который поместить только строки из my_list.



my_list = [1, 2, 3, "11", "22", 33, "juhi"]
new_list = []

for element in my_list:
    if type(element) is str:
        new_list.append(element)
print(new_list)



# # 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# # которые встречаются в строке ТОЛЬКО ОДИН раз.



my_str = "qweewewqeqwwewerwqqqq"

for symbol in my_str:
    count_symbol = my_str.count(symbol)
    if count_symbol == 1:
        print(symbol)


# # 6. Даны две строки. Создать список в который поместить те символы,
# # которые есть в обеих строках хотя бы раз.



my_str_1 = "qweewewqeqwwewerwqqqq"
my_str_2 = "qweefkllkewjblvjqwwfjnvlewqq"

my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)

intersection_of_sets = list(my_set_1.intersection(my_set_2))
print(intersection_of_sets)



# # 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# # но в каждой ТОЛЬКО ПО ОДНОМУ разу.



my_str_1 = "zqweewewq8eqwweywerwqqqq"
my_str_2 = "qzweefkllkewjbly8vjqwwfjnvlewqq"
my_list = []

my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)

intersection_of_sets = list(my_set_1.intersection(my_set_2))

for element in intersection_of_sets:
    count_1 = my_str_1.count(element)
    count_2 = my_str_2.count(element)
    if count_1 == 1 and count_2 == 1:
        my_list.append(element)
print(my_list)



# # 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# # Фамилия
# # Имя
# # Возраст
# # Проживание
# #     Страна
# #     Город
# #     Улица
# # Работа
# #     Наличие
# #     Должность



person = {"Person": {"Фамилия": "Bakanova",
                    "Имя": "Valeriia",
                    "Возраст": 31},
          "Проживание": {"Страна": "Ukraine",
                         "Город": "Dnipro",
                         "Улица": "Artekivska"},
          "Работа": {"Наличие": "+",
                     "Должность": "Manual QA"}}



# # # 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# # # придумать и указать граммы для продуктов):
# # # Составляющие
# # #     Коржи
# # #         Мука
# # #         Молоко
# # #         Масло
# # #         Яйцо
# # #     Крем
# # #         Сахар
# # #         Масло
# # #         Ваниль
# # #         Сметана
# # #     Глазурь
# # #         Какао
# # #         Сахар
# # #         Масло



cake = {"Составляющие": {"Коржи": {"Мука": 1000,
                                   "Молоко": 500,
                                   "Масло": 200,
                                   "Яйцо": 150},
                         "Крем": {"Сахар": 250,
                                  "Масло": 400,
                                  "Ваниль": 7,
                                  "Сметана": 500},
                         "Глазурь": {"Какао": 40,
                                     "Сахар": 60,
                                     "Масло": 50}}}
