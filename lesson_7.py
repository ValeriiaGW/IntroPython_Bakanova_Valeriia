
my_str = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"

result_1 = []
for symbol in my_str:
    if symbol.islower():
        result_1.append(symbol)
str_1 = "".join(result_1)
print(str_1)

str_2 = ""
for symbol in my_str:
    if symbol.islower():
        str_2 += symbol
print(symbol)



##################################################

# Составить строку из маленьких согласных букв
my_str = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"

# result_1 = []
# for symbol in my_str:
#     if symbol.islower() and not in "eyuioa":
#         str_2 += symbol
# print(str_2)

##########################################
str_3 = ""
for symbol in my_str:
    if symbol.islower():
        str_3 += symbol.upper()
    elif symbol.isupper():
        str_3 += symbol.lower()
    else:
        str_3 += symbol


#########################################
big_letters = []
little_a_letter = []
little_b_letter = []
symbols = []

for symbol in my_str:
    if symbol.isupper():
        big_letters.append(symbol)
    elif symbol.islower():

        ## HW #5
        # 1. Дано целое число (int). Определить сколько нулей в этом числе.

        my_number = 1276000351725300700000
        zero_count = str(my_number).count("0")
        print(zero_count)
        # 2. Дано целое число (int). Определить сколько нулей в конце этого числа. Например для числа 1002000 - три нуля

        str_number = str(my_number)
        # zero_count = len(str_number) - len(str_number.rstrip("0"))
        zero_count = len(str_number) - len(str(int(str_number[::-1])))
        print(zero_count)

        # 3. Даны списки my_list_1 и my_list_2.
        # Создать список my_result в который вначале поместить
        # элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
        my_list_1 = [1, 21, 31, 41]
        my_list_2 = [2, 22, 32, 42]
        my_result = []
        for index, value in enumerate(my_list_1):
            if not index % 2:
                my_result.append(value)
        for index, value in enumerate(my_list_2):
            if index % 2:
                my_result.append(value)
        print(my_result)

        my_result = my_list_1[::2] + my_list_2[1::2]
        print(my_result)

        # 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
        # стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

        my_list = [1, 21, 31, 41]
        print(id(my_list))
        new_list = my_list[1:]
        new_list.append(my_list[0])
        print(new_list, id(new_list), my_list)

        # 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
        # [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

        my_list.append(my_list.pop(0))
        print(id(my_list), my_list)
        # 6. Дана строка в которой есть числа (разделяются пробелами).
        # Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
        # Для данного примера ответ - 133. (используйте split и проверку isdigit)
        my_str = "43 больше чем 34 но меньше чем     56"
        parts = my_str.split()
        print(parts)
        sum_numbers = 0
        for sub_str in parts:
            if sub_str.isdigit():
                sum_numbers += int(sub_str)
        print(sum_numbers)

        numbers = []
        for sub_str in parts:
            if sub_str.isdigit():
                numbers.append(int(sub_str))
        sum_numbers = sum(numbers)
        print(sum_numbers)

        print(sum([int(sub_str) for sub_str in parts if sub_str.isdigit()]))

        # 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
        # которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
        # В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
        # my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

        my_str = "My long string"
        l_limit = "o"
        r_limit = "g"
        index_l = my_str.find(l_limit)
        index_r = my_str.rfind(r_limit)
        sub_str = my_str[index_l + 1:index_r]
        print(sub_str)

        # 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
        # Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
        # быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
        # (используйте срезы длинны 2)

        my_str = 'abcdeas'
        if len(my_str) % 2:
            my_str += "_"
        res = []
        for index in range(len(my_str) // 2):
            sub_str = my_str[2 * index: 2 * index + 2]
            res.append(sub_str)
        print(res)

        # 9. Дан список чисел. Определите, сколько в этом списке элементов,
        # которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
        # Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
        # Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

        my_list = [2, 4, 1, 5, 3, 9, 0, 7]
        result_list = []
        for index in range(1, len(my_list) - 1):
            if my_list[index] > my_list[index - 1] + my_list[index + 1]:
                result_list.append(my_list[index])
        result = len(result_list)
        print(result)

        #### HW #4
        # 1) У вас есть список my_list с значениями типа int.
        # Распечатать те значения, которые больше 100.
        # Задание выполнить с помощью цикла for.
        my_list = [12, 34, -2, 124, 962, 0]
        for value in my_list:
            if value > 100:
                print(value)

        # 2) У вас есть список my_list с значениями типа int, и пустой список my_results.
        # Добавить в my_results те значения, которые больше 100.
        # Распечатать список my_results.
        # Задание выполнить с помощью цикла for.

        my_list = [12, 34, -2, 124, 962, 0]
        my_results = []
        for value in my_list:
            if value > 100:
                my_results.append(value)
        print(my_results)

        # 3) У вас есть список my_list с значениями типа int.
        # Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
        # Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
        # Количество элементов в списке можно получить с помощью функции len(my_list)

        my_list = [12, 34, -2, 124, 962, 10]
        if len(my_list) >= 2:
            my_list.append(my_list[-1] + my_list[-2])
        else:
            my_list.append(0)
        print(my_list)

        # 4) Пользователь вводит value - число с запятой (например 3.14) с клавиатуры.
        # Вы приводите это value к типу float и выводите результат выражения value ** -1.
        # Написать программу, которая вычисляет данное выражение и
        # корректно обрабатывает возможные исключения.
        value = input("Введи float")
        try:
            value = float(value)
            result = value ** -1
        except ValueError:
            print("Это не float")
        except ZeroDivisionError:
            print("Введи не ноль")

        # #####################################################
        # 5) У вас есть строка my_string = '0123456789'.
        # Сгенерировать целые числа (тип int) от 0 до 99 и ПОМЕСТИТЬ их в список.
        # Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов.
        # Генерирование через range или другие "фишки" я засчитывать не буду ))
        my_string = '0123456789'
        result = []

        for symb_1 in my_string:
            for symb_2 in my_string:
                result.append(int(symb_1 + symb_2))

        print(result)

        # Дана строка My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!
        # Составить строку из больших букв этого предложения
        # Составить строку из маленьких букв этого предложения
        # Составить строку из больших гласных букв этого предложения
        # Составить строку из маленьких согласных букв этого предложения
        # Составить строку из букв этого предложения, заменив большие буквы на маленькие и наоборот
        # Составить строку из символов этого предложения по следующему правилу:
        # Большие буквы в алфавитном порядке. Затем маленькие гласные буквы в алфавитном порядке.
        # Потом маленькие согласные буквы в алфавитном порядке.
        # Затем другие символы в порядке, в котором они есть в предложении.

        my_str = "My name is Vova. I'm 41. But I still believe in magic. EXPELLIARMUS!"

        result_1 = []
        for symbol in my_str:
            if symbol.islower():
                result_1.append(symbol)
        result_1 = [symbol for symbol in my_str if symbol.isupper()]
        str_1 = "".join(result_1)
        print(str_1)

        # Составить строку из маленьких согласных букв этого предложения
        str_2 = ""
        for symbol in my_str:
            if symbol.islower() and symbol not in "eyuioa":
                str_2 += symbol
        print(str_2)

        # Составить строку из букв этого предложения, заменив большие буквы на маленькие и наоборот
        print(my_str.swapcase())
        str_3 = ""
        for symbol in my_str:
            if symbol.islower():
                str_3 += symbol.upper()
            else:
                str_3 += symbol.lower()
            # elif symbol.isupper():
            #     str_3 += symbol.lower()
            # else:
            #     str_3 += symbol
        print(str_3)

        # Составить строку из символов этого предложения по следующему правилу:
        # Большие буквы в алфавитном порядке. Затем маленькие гласные буквы в алфавитном порядке.
        # Потом маленькие согласные буквы в алфавитном порядке.
        # Затем другие символы в порядке, в котором они есть в предложении.

        big_letters = []
        little_a_letter = []
        little_b_letter = []
        symbols = []

        for symbol in my_str:
            if symbol.isupper():
                big_letters.append(symbol)
            elif symbol.islower() and symbol in "eyuioa":
                little_a_letter.append(symbol)
            elif symbol.islower() and symbol not in "eyuioa":
                little_b_letter.append(symbol)
            else:
                symbols.append(symbol)
        result = sorted(big_letters) + sorted(little_a_letter) + sorted(little_b_letter) + symbols
        res_str = "".join(result)
        print(res_str)

        # так не рекоменндую делать
        # for symbol in my_str:
        #     if symbol.isupper():
        #         big_letters.append(symbol)
        #     elif symbol.islower():
        #         if symbol in "eyuioa":
        #             little_a_letter.append(symbol)
        #         else:
        #             little_b_letter.append(symbol)
        #     else:
        #         symbols.append(symbol)
        # result = sorted(big_letters) + sorted(little_a_letter) + sorted(little_b_letter) + symbols
        # res_str = "".join(result)
        # print(res_str)
