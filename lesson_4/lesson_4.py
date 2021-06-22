# value = input("Введи целое число")
# if value.isdigit():
#     value = int(value)
#     result = value * 2
#     print(result)
# else:
#     print("Вы ввели не число")



# value = input("Введи целое число")
# try:
#     value = float(value)
#     result = value * 2
#     print(result)
# except:
#     print("Число не может быть приведено к типу float")



# value = input("Введи целое число")
# try:
#     value = float(value)
#     result = value * 2
# except:
#     print("Число не может быть приведено к типу float")
#     result = 0
# print(result)



# value = input("Введи целое число")
# try:
#     value = float(value)
#     result = 1 / value
# except ValueError:
#     print("Число не может быть приведено к типу float")
#     result = 0
# except ZeroDivisionError:
#     print("на ноль делить нельзя")
#
# print(result)



# value = input("Введи целое число")      # some error
# try:
#     value = float(value)
#     result = 1 / value
# except (ValueError, ZeroDivisionError):
#     print("???")
#     result = 0
# print(result)

# ИТЕРАЦИЯ

# count = 10
# while count > 0:
#     # count += 1 # увеличение НА 1
#     count -=1 # уменьшение НА 1
#     print(f"count = {count}")
# print("The end!")



# tmp_value = 5
#
# go_game = True
#
# while go_game:
#     value = input("введи число от 1 до 10")
#     if str(tmp_value) == value:# не забыть приобразовать вэлью в строку, для сравнения строки со строкой
#         go_game = False
#         print("Ура, угадал!!!")


# break как вариант, но лучше не пользоваться
# tmp_value = 5
#
# while True:
#     value = input("введи число от 1 до 10")
#     if str(tmp_value) == value:# не забыть приобразовать вэлью в строку, для сравнения строки со строкой
#         print("Ура, угадал!!!")
#         break



# Цикл For
#
# test_str = "qwerty"
#
# for symbol in test_str:
#     print(f"symbol: {symbol}")
#
#
# test_str = "qwerty"
#
# for symbol in test_str[::-1]: # в обратном порядке
#     print(f"symbol: {symbol}")
#

# только гласные буквы

# test_str = "qwertyamdlkmknadmDRYLoiuhbnm"
#
# for symbol in test_str:
#     if symbol not in "eyaoiu":
#         print(f"symbol: {symbol}")

# только гласные буквы чтоб все буквы были одного регистра

# test_str = "qwertyamdlkmknadmDRYLoiuhbnm"
#
# for symbol in test_str:
#     if symbol.lower() not in "eyaoiu":
#         print(f"symbol: {symbol}")

# исключить символы
# test_str = "qwertyamdlkmknadmDRYLo///'';;uhbnm"
#
# for symbol in test_str:
#     if symbol.lower() not in "eyaoiu" and symbol.isalpha():
#         print(f"symbol: {symbol}")



# tuple - кортеж - неизменяемый тип (перечисление по умолчанию, защита от записи, зазмер памяти)
# list - список - изменяемый тип


# my_list[index] - обращение по индексу

# my_tuple = (1, 2, "tuple", (-1,0), None)
# print(type(my_tuple), my_tuple)
#
# my_list = [1, 2, "list", (-1, 0), None]
# print(type(my_list), my_list)
#
# index = 2 #срез
# value_tuple = my_tuple[index]
# value_list = my_list[index]
# print(value_tuple, value_list)
#
#
#
# index = -1
# my_list [index] = 3
# value_tuple = my_tuple[index]
# my_list = my_list[index]
# print(value_tuple, value_list)
# print(type(my_list), my_list)
# срезы как в строках







# my_tuple = (1, 2, "tuple", (-1,0), None)
# print(type(my_tuple), my_tuple)
#
# my_list = [1, 2, "list", (-1, 0), None]
# print(type(my_list), my_list)
#
# index = 1
# value_tuple = list(my_tuple)
# my_tuple[index] = 'NEW_VALUE'
# my_tuple = tuple(my_tuple)
#
# # приведение к типам
# new_list = list(my_tuple)
# new_tuple = tuple(my_list)
# print("new_list", type(new_list), new_list)
# print("new_tuple", type(new_tuple), new_tuple)  # some error


new_list = []

some_value = new_list.append('first')
new_list.append('second')
new_list.append([1,3,5])
last_value = new_list.pop()
print(new_list)
print(last_value, some_value)


#
# test_str = "qwertyamdlkmknadmDRYLoiuhbnm"
# result = []
# for symbol in test_str:
#     if symbol.lower() not in "eyaoiu" and symbol.isalpha():
#         # print(f"symbol: {symbol}")
#         result.append(symbol)
#     print(result)

# join_str = "_".join(result)
# print(join_str)
#
# join_str = "".join(result)
# print(join_str)
#
# split_str = list(test_str)
# print(split_str)