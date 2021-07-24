persons = [
    {"name": "Jon", "age": 15},
    {"name": "Mike", "age": 35},
    {"name": "Anna", "age": 15},
    {"name": "Samanta", "age": 75},
    {"name": "Jack", "age": 45},
]
age_list = []
names_length = []

for person in persons:

    age = person.get("age")
    age_list.append(age)
    long_name = len(person.get("name"))
    names_length.append(long_name)

min_age = min(age_list)

for person in persons:
    if person.get("age") == min_age:
        print(person.get("name"))

max_name_length = max(names_length)

for person in persons:
    if len(person.get("name")) == max_name_length:
        print(person.get("name"))

sum_age = sum(age_list)
avg_age = sum_age / len(age_list)
print(avg_age)


# min_age = persons[0].get("age")
# long_name = len(persons[0].get("name"))
# sum_age = 0
#
# for person in persons:
#     age = person.get("age")
#     if age < min_age:
#         min_age = age
# for person in persons:
#     if min_age == person.get("age"):
#         print(person.get("name"))
#
# for person in persons:
#     if len(person.get("name")) > long_name:
#         long_name = len(person.get("name"))
# for person in persons:
#     if len(person.get("name")) == long_name:
#         print(person.get("name"))
#
# for person in persons:
#     sum_age += person.get("age")
#
#     avg_are = sum_age / len(persons)


# persons = {"John": 12, "Jack": 34, "Anna": 27}


# persons["Jackob"] = 59
# persons["John"] = len("Test")


# result = "Anna" in persons  # in проверяет ТОЛЬКО КЛЮЧИ!!
#
# key = "Anna"
#
# for key in persons:
#     print(key, persons[key])
# value = persons.pop("Jackob")
# print(">>>>>", value)
# for key, value in persons.items():
#     print(key, value)


# max_age = max(persons.values())
# print(max_age)