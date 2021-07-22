import os

current_dir = os.getcwd()
print(current_dir)

list_dir = os.listdir()
print(list_dir)



import os


# current_dir = os.getcwd()
# print(current_dir)
# tmp_path = os.path.join(current_dir, "Homeworks", "tmp", "test_2")
# print(tmp_path)

def get_files_from_dir(base_dir, full_path=True):
    list_dir = os.listdir(base_dir)
    files = []
    for file_object in list_dir:
        path_object = os.path.join(base_dir, file_object)
        if os.path.isfile(path_object):
            files.append(path_object if full_path else file_object)
    return files


# alphabet_files = get_files_from_dir("alphabet")
# print(alphabet_files)
# homeworks_files = get_files_from_dir("Homeworks", full_path=False)
# print(homeworks_files)

# def create_dir(path):
#     try:
#         os.mkdir(path)
#     except FileExistsError:
#         pass


# os.makedirs("test_3_dir/test_4_dir", exist_ok=True)




# with open("lesson10.py", "r") as py_file:
#     data = py_file.readlines()
#
# print(data, type(data))
#
# data.append("# FINISH\n")
# with open("lesson10_new.py", "w") as py_file:
#     py_file.writelines(data)

with open("Homeworks/names.txt", "r") as txt_file:
    data = txt_file.readlines()

for line in data:
    if len(line) > 32:
        print(line.split("\t"))





################################################
# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
import string


def create_dir(path):
    os.makedirs(path, exist_ok=True)


def create_file(path, symbol):
    filename = f"{path}/{symbol}.txt"
    with open(filename, 'w') as txt_file:
        txt_file.write(string.ascii_lowercase.replace(symbol, symbol.upper()))


def create_files_in_dir(path):
    for letter in string.ascii_lowercase:
        create_file(path, letter)


def get_tanos_click(path):
    files = os.listdir(path)
    files = list(set(files))[:len(files) // 2]
    for file in files:
        os.remove(os.path.join(path, file))


# create_dir("alphabet")
create_files_in_dir("alphabet")
get_tanos_click("alphabet")