# ДЗ: давать подсказку типа: "Попробуй больше", "Попробуй меньше", чтоб

tmp_value = 5

go_game = True

while go_game:
    value = input("введи число от 1 до 10")
    if str(tmp_value) == value:
        go_game = False
        print("Ура, угадал!!!")
    elif str(tmp_value) < value:
        value = input("Попробуй меньше")
        # print("Попробуй меньше")
    elif str(tmp_value) > value:
        print("Попробуй больше")