# ДЗ: давать подсказку типа: "Попробуй больше", "Попробуй меньше", чтоб

# tmp_value = 5
# go_game = True
# value = int(input("введи число от 1 до 10: "))
# while go_game:
#     if tmp_value == value:
#         go_game = False
#         print("Ура, угадал!!!")
#     if tmp_value < value:
#         value = int(input("попробуй меньше: "))
#     if tmp_value > value:
#         value = int(input("попробуй больше: "))       # моё решение


# tmp_value = 5
# go_game = True
# text_message = "введи число от 1 до 10: "
# while go_game:
#     try:
#         value = int(input(text_message))
#         if tmp_value > value:
#             text_message = "попробуй больше"
#         elif tmp_value < value:
#             text_message = "попробуй меньше"
#         else:
#             go_game = False
#             print("Ура, угадал")
#     except ValueError:
#         text_message = "введи число от 1 до 10:"



# сколько раз символ встрречается в строке

# my_str = "blablacar"
# my_symbol = "bla"
#
# my_symbol_count = my_str.count(my_symbol)
# print(my_symbol_count)


# напечать столько раз символ сколько раз он встречается в строке, вывод на экран в столбик

# my_str = "blablacar"
# my_symbol = "bla"
#
# my_symbol_count = my_str.count(my_symbol)
#
# # print(my_symbol * my_symbol_count)  # выводит результат в строку
#
# for index in range (my_symbol_count):
#     # pass # заглушка, если после for не надо ничего выполнять
#     print(my_symbol)

 # print(f"{my_symbol}\n" * my_symbol_count) # как вариант с ф-строкой и переносом на сл строчку



# Число разных символов которые встречаются в строке. большая и маленькая буквы считаются как один символ
# пробелы и спецсимволы тоже считаются

my_str = "bla BLA car"
my_str = my_str.lower()
symbols_heap = []
for symbol in my_str:
    if symbol not in symbols_heap:
        symbols_heap.append(symbol)
res_len = len(symbols_heap)
print(res_len)