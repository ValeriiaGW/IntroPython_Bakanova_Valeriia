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


