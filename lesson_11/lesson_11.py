# json, csv
# импорт из файла
# assert
import json
import csv


from lesson11_csv import read_from_csv

def write_json(filename, data):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)


def read_json(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
        return data


data_list = [1, 2, 3, 4, 5]
data_dict = {"name": "John",
             "age": 13,
             "job": {"title": "Data Ingener",
                     "price": "1000$"}}
# data_dumps = json.dumps(data)
# print(data_dumps, type(data_dumps))

filename = "data_dict.json"
write_json(filename, data_dict)
data = read_json(filename)
print(data, type(data))


filename = "new_data_2.csv"
new_data = read_from_csv(filename)
print(new_data)


def write_to_csv(filename, data, delimiter=","):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
        return data

filename = "data.csv"
# data_2 = [[1, 2, 3], [4, 5, 6], [12, 13, 14]]
# write_to_csv(data=data_2, filename=filename)  #  именованная передача аргументов
# write_to_csv(filename, delimiter=";", data=data_2)  # позиционная передача аргументов

new_data = read_from_csv(filename)

print("---->", new_data)

new_data[0].append("Sum")
for row in new_data[1:]:
    row.append(int(row[-2]) + int(row[-1]))

# new_data.append([100,200,300])
write_to_csv(data=new_data, filename="new_data.csv")




def read_dict_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
    return data


def write_dict_to_csv(filename, data):
    fieldnames = ["Monts", "Amount", "Total", "Percentage", "Sum"]  # data[0].keys()
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()  # записывает заголовок
        writer.writerows(data)


filename = "new_data.csv"
new_data = read_dict_from_csv(filename)
for row in new_data:
    row["Percentage"] = int(row["Sum"]) * 0.2
# print(new_data)
filename = "new_data_2.csv"
write_dict_to_csv(filename, new_data)



def read_dict_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
    return data


def read_from_csv(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        data = []
        for row in reader:
            data.append(row)
        return data


def write_dict_to_csv(filename, data):
    fieldnames = ["Monts", "Amount", "Total", "Percentage", "Sum"]  # data[0].keys()
    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()  # записывает заголовок
        writer.writerows(data)


def write_to_csv(filename, data, delimiter=","):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=delimiter)
        writer.writerows(data)


print(__name__)
if __name__ == "__main__":
    filename = "new_data_2.csv"
    new_data = read_from_csv(filename)
    print(new_data)



from tools import read_from_csv

filename = "new_data.csv"
new_data = read_from_csv(filename)
assert len(new_data[0]) == 4
print(new_data)