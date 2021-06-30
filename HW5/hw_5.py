# 1. Дано целое число (int). Определить сколько нулей в этом числе.

# my_value = 90890239989793789
# my_value = str(my_value)
# my_symbol = "0"
# my_symbol_count = my_value.count(my_symbol)
# print(my_symbol_count)
#


# 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля
#
# my_value = 9089023998979378900000000
# count_zero = 0
# while my_value % 10 == 0:
#     count_zero += 1
#     my_value = my_value // 10
# print(count_zero)


# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
# #
# my_list_1 = ["s", "f", "g", "t"]
# my_list_2 = ["a", "b", "c", "d"]
# my_result = []
#
# for i in range(len(my_list_1)):
#     if i % 2:
#         my_result.append(my_list_1[i])
#
# for i in range(len(my_list_2)):
#     if not i % 2:
#         my_result.append(my_list_2[i])
#
# print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

# my_list = ["1", "2", "3", "4"]
# new_list = my_list.copy()
# first_elem = new_list.pop(0)
# new_list.append(first_elem)
# print(new_list, my_list)
#
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

# my_list = ["1", "2", "3", "4"]
# first_elem = my_list.pop(0)
# my_list.append(first_elem)
# print(my_list)
#
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
#

# my_str = "43 больше чем 34 но меньше чем 56"
# my_value = sum(int(s) for s in my_str.split() if s.isdigit())
# print(my_value)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

# my_str = "My long string"
# l_limit = "o"
# r_limit = "g"
#
# l_limit_index = my_str.find(l_limit)
# r_limit_index = my_str.rfind(r_limit)
# sub_str = my_str[l_limit_index + 1:r_limit_index]
# print(sub_str)




# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
#
my_str = "qwertyhbvcqxqttzqr"
new_list_1 = []

if len(my_str) % 2 != 0:
    my_str = my_str + "_"

for i in range(1, len(my_str), 2):
    # new_str = my_str[i-1] + my_str[i]
    new_str = my_str[i-1:i+1]
    new_list_1.append(new_str)

print(new_list_1)




# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

