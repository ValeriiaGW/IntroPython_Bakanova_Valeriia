
# my_list = [2, 4, 56, 76, 66, 656, 544, 333, 234]
# for i in my_list:
#     if i > 100:
#         print(i)



# my_list = [2, 4, 56, 76, 66, 656, 544, 333, 234]
# my_results = []
# for i in my_list:
#     if i > 100:
#         new_list = i
#         my_results.append(new_list)
# print(my_results)


# my_list = [435]
# if len(my_list) >= 2:
#     my_list.append(my_list[-1] + my_list[-2])
# else:
#     my_list.append(0)
# print(my_list)



# value = input("введи дробное число: ")
# try:
#     value = float(value)
#     new_value = value ** -1
# except (ValueError, ZeroDivisionError):
#     print("Введено не число или ноль")
#     exit(1)
# print(new_value)




#
# #####################################################
# Еще один пример - вложенные циклы (цикл в цикле).
my_string_1 = "ab"
my_string_2 = "cd"
for symb_1 in my_string_1:
	for symb_2 in my_string_2:
		print(symb_1 + symb_2)
#
#
#
# Результат:
# "13"	# перебирается все элементы из my_string_2 для элемента "1" из my_string_1
# "14"
# "23"	# перебирается все элементы из my_string_2 для элемента "2" из my_string_1
# "24"
# #####################################################
#
# 5) У вас есть строка my_string = '0123456789'.
# Сгенерировать целые числа (тип int) от 0 до 99 и ПОМЕСТИТЬ их в список.
# Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
# Генерирование через range или другие "фишки" я засчитывать не буду ))

my_string = '0123456789'
my_int = int(my_string)
for i in my_int:
	for