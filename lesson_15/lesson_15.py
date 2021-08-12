# 1. Создать папку ./alphabet/ или проверить, что папка существует.
# 2. В папку ./alphabet/ поместить файлы вида a.txt, b.txt, ..., z.txt
# в которых будет записана строка алфавита, но с заменой буквы из названия файла на прописную.
# Пример: для b.txt строка будет aBcde...
# 3. Сделать щелчек Таноса - удалить случайным образом половину всех файлов в этой папке.
import os
# import string
from string import ascii_lowercase as alphabet

# область видтмости класса

class WorkWithFiles:
    def __init__(self, dirname="alphabet"):
        self.dirname = dirname
        self.create_dir()


    def create_dir(self):
        os.makedirs(self.dirname, exist_ok=True)


    def create_file(self, symbol):
        filename = f"{self.dirname}/{symbol}.txt"
        with open(filename, 'w') as txt_file:
            txt_file.write(alphabet.replace(symbol, symbol.upper()))


    def create_files_in_dir(self):
        for letter in alphabet:
            self.create_file(letter)


    def get_tanos_click(self):
        files = os.listdir(self.dirname)
        files = list(set(files))[:len(files) // 2]
        for file in files:
            os.remove(os.path.join(self.dirname, file))


file_worker = WorkWithFiles("qwe")

print(file_worker.dirname)
# file_worker.create_files_in_dir()  # создает файлы
file_worker.get_tanos_click() # удаляет половину файлов