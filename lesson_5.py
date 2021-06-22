# ДЗ: давать подсказку типа: "Попробуй больше", "Попробуй меньше", чтоб

tmp_value = 5

go_game = True

value = int(input("введи число от 1 до 10: "))

while go_game:
    if tmp_value == value:
        go_game = False
        print("Ура, угадал!!!")
    if tmp_value < value:
        value = int(input("попробуй меньше: "))
    if tmp_value > value:
        value = int(input("попробуй больше: "))


