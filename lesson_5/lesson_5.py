# # ДЗ: давать подсказку типа: "Попробуй больше", "Попробуй меньше", чтоб
#
# # tmp_value = 5
# # go_game = True
# # value = int(input("введи число от 1 до 10: "))
# # while go_game:
# #     if tmp_value == value:
# #         go_game = False
# #         print("Ура, угадал!!!")
# #     if tmp_value < value:
# #         value = int(input("попробуй меньше: "))
# #     if tmp_value > value:
# #         value = int(input("попробуй больше: "))       # моё решение
#
#
# # tmp_value = 5
# # go_game = True
# # text_message = "введи число от 1 до 10: "
# # while go_game:
# #     try:
# #         value = int(input(text_message))
# #         if tmp_value > value:
# #             text_message = "попробуй больше"
# #         elif tmp_value < value:
# #             text_message = "попробуй меньше"
# #         else:
# #             go_game = False
# #             print("Ура, угадал")
# #     except ValueError:
# #         text_message = "введи число от 1 до 10:"
#
#
#
# # сколько раз символ встрречается в строке
#
# # my_str = "blablacar"
# # my_symbol = "bla"
# #
# # my_symbol_count = my_str.count(my_symbol)
# # print(my_symbol_count)
#
#
# # напечать столько раз символ сколько раз он встречается в строке, вывод на экран в столбик
#
# # my_str = "blablacar"
# # my_symbol = "bla"
# #
# # my_symbol_count = my_str.count(my_symbol)
# #
# # # print(my_symbol * my_symbol_count)  # выводит результат в строку
# #
# # for index in range (my_symbol_count):
# #     # pass # заглушка, если после for не надо ничего выполнять
# #     print(my_symbol)
#
#  # print(f"{my_symbol}\n" * my_symbol_count) # как вариант с ф-строкой и переносом на сл строчку
#
#
#
# # Число разных символов которые встречаются в строке. большая и маленькая буквы считаются как один символ
# # пробелы и спецсимволы тоже считаются
#
# my_str = "bla BLA car"
# my_str = my_str.lower()
# symbols_heap = []
# for symbol in my_str:
#     if symbol not in symbols_heap:
#         symbols_heap.append(symbol)
# res_len = len(symbols_heap)
# print(res_len)
#
#
# # дана строка и пустой список, заполнить список символами из строки, которые стоят на четных местах в строке
#
# # my_str = "qwerty"
# # my_list = []
# # for index in range(len(my_str)):
# # 	if not index % 2:
# # 		symbol = my_str[index]
# # 		my_list.append(symbol)
# # print(my_list)         # №1
#
# #
# # my_str = "qwerty"
# # my_list = []
# #
# # for index, symbol in enumerate(my_str):
# # 	if not index % 2:
# # 		my_list.append(symbol)
# #
# # print(my_list)			# №2
#
#
# # дана строка и список цулых чисел в диапазоне от 0 до длины строки -1 и пустой список
# # заполнить список символами которые стоят на местах с индексами из строки
# #
# # my_str = "qwerty"
# # my_list = []
# # str_index = [3, 4, 5, 6, 0, 0, 1]
# #
# # for index in str_index:
# #     symbol = my_str[index]
# #     my_list.append(symbol)
# # print(my_list)
#
#
# # дано целое число инт определить сколько цифр в этом числе
# #
# # my_number = 8765432123456765
# # digit_count = len(str(my_number))
# # print(digit_count)
#
#
# # дано целое число определить наибольшую цифру в этом числе
#
# # my_number = 8765432123456765
# # number_str = str(my_number)
# # max_symbol = max(number_str)
# # print(max_symbol)
#
#
#  # дано цулое число. составить число с цифрами в обратном порядке
#
# # my_number = 8765432123456765
# # number_str = str(my_number)
# # new_number_str = number_str[::-1]
# # new_number = int(new_number_str)
# # print(new_number)
#
# # дано целое число составить число с цифрами в порядке возростания/убывания
#
# # my_list = [1, 2, 5, 3, -8, 4]
# # sorted_list = sorted(my_list)
# # print(sorted_list)                 # сортировка по возрастанию
#
#
# # my_list = [1, 2, 5, 3, -8, 4]
# # sorted_list = sorted(my_list, reverse=True)
# # print(sorted_list)                  # сортировка по убыванию
#
#
#
# # my_str = 'qwerty'
# # sorted_list = sorted(my_str)
# # print(sorted_list)
#
# my_number = 876543201234056765
# number_str = str(my_number)
# sorted_number_symbols_list = sorted(number_str)
# new_number_str = ''.join(sorted_number_symbols_list)
# new_number = int(new_number_str)
# print(new_number)
#
#
# # extra task: написать последний код одной строкой
# my_number = 876543201234056765
# new_number = int(''.join(sorted(str(my_number))))
# print(new_number)