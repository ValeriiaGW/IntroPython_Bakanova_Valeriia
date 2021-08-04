# # # # # # # # # # класс
# # # # # # # # # # атрибут класса
# # # # # # # # # # экземпляр класса
# # # # # # # # # # атрибут экземпляра класса
# # # # # # # # # # метод экземпляра класса
# # # # # # # # #
# # # # # # # # # # # class MyFirstClass:
# # # # # # # # # # #     some_string = "TEST"
# # # # # # # # # # #
# # # # # # # # # # # test_value = MyFirstClass.some_string
# # # # # # # # # # # print(test_value)
# # # # # # # # # #
# # # # # # # # # #
# # # # # # # # # # class MyFirstClass:
# # # # # # # # # #     some_string = "TEST"        # атрибут класса
# # # # # # # # # #     value = 0                   # атрибут класса
# # # # # # # # # #
# # # # # # # # # # MyFirstClass.some_string = "new test"
# # # # # # # # # # test_value = MyFirstClass.some_string
# # # # # # # # # # print(test_value)
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # class Person:
# # # # # # # # #     name = "John"
# # # # # # # # #     surname = "Wick"
# # # # # # # # #     age = 23
# # # # # # # # #     sex = "Male"
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # if Person.age < 50:
# # # # # # # # #     print(f"Ты молодой человек, {Person.name} {Person.surname}")
# # # # # # # #
# # # # # # # #
# # # # # # # # class Person:
# # # # # # # #     name = "John"
# # # # # # # #     surname = "Wick"
# # # # # # # #     age = 23
# # # # # # # #     sex = "Male"
# # # # # # # #
# # # # # # # #
# # # # # # # # person_1 = Person()     # экземпляр класса
# # # # # # # # person_2 = Person()     # экземпляр класса
# # # # # # # # person_1.name = "Vova"
# # # # # # # # print(person_1.name)
# # # # # # # # print(person_2.name)
# # # # # # #
# # # # # # #
# # # # # # # class Person:
# # # # # # #     name = "John"
# # # # # # #     surname = "Wick"
# # # # # # #     age = 23
# # # # # # #     sex = "Male"
# # # # # # #
# # # # # # #
# # # # # # # person_1 = Person()
# # # # # # # person_2 = Person()
# # # # # # #
# # # # # # # print(person_1.name)
# # # # # # # print(person_2.name)
# # # # # # # print('-----------------')
# # # # # # # person_1.name = "Vova"
# # # # # # # print(person_1.name)
# # # # # # # print(person_2.name)
# # # # # # # print('-----------------')
# # # # # # # Person.name = "Jack"
# # # # # # # print(person_1.name)
# # # # # # # print(person_2.name)
# # # # # #
# # # # # #
# # # # # # class Person:
# # # # # #     name = "John"
# # # # # #     surname = "Wick"
# # # # # #     age = 23
# # # # # #     sex = "Male"
# # # # # #
# # # # # #
# # # # # # person_1 = Person()
# # # # # # person_2 = Person()
# # # # # #
# # # # # # print(person_1.name)
# # # # # # print(person_2.name)
# # # # # # print('-----------------')
# # # # # # person_1.name = "Vova"
# # # # # # print(person_1.name)
# # # # # # print(person_2.name)
# # # # # # print('-----------------')
# # # # # # Person.name = "Jack"
# # # # # # print(person_1.name)
# # # # # # print(person_2.name)
# # # # # #
# # # # # #
# # # # # #
# # # # # # person_1.address = 'Dnipro'
# # # # # # print(person_1.address)
# # # # # # #####################################################################
# # # # # #
# # # # # class Person:
# # # # #     def __init__(self):
# # # # #         self.name = "John"
# # # # #
# # # # # person_1 = Person()
# # # # # person_2 = Person()
# # # # #
# # # # # print(person_1.name)
# # # # # print(person_2.name)
# # # # #
# # # # class Person:
# # # #     def __init__(self, name):
# # # #         self.name = name
# # # #
# # # #
# # # # person_1 = Person("John")
# # # # person_2 = Person("Jack")
# # # #
# # # # print(person_1.name)
# # # # print(person_2.name)
# # #
# # #
# # # class Person:
# # #     def __init__(self, name, surname, age, sex):
# # #         self.name = name
# # #         self.surname = surname
# # #         self.age = age
# # #         self.sex = sex
# # #
# # #     def __str__(self):
# # #         # return self.name
# # #         return f"{self.name} {self.surname}, {self.age}"
# # #
# # # person_1 = Person("John", "Wick", 23, "Male")
# # # person_2 = Person("Jane", "Ostin", 32, "Female")
# # #
# # # print(person_1)
# # # print(person_2)
# # #
# #
# # class Person:
# #     def __init__(self, name, surname, age, sex):
# #         self.name = name
# #         self.surname = surname
# #         self.age = age
# #         self.sex = sex
# #
# #     def __str__(self):
# #         # return self.name
# #         return f"{self.name} {self.surname}, {self.age}, {self.sex}"
# #
# #     def __repr__(self):
# #         return f"{self.name} {self.surname}"
# #
# # person_1 = Person("John", "Wick", 23, "Male")
# # person_2 = Person("Jane", "Ostin", 32, "Female")
# #
# # list_persons = [person_1, person_2]
# #
# # print(person_1)   #------> __str__(self)
# # print(person_2)
# # print(list_persons)     #------> __repr__(self)
#
#
#
#
## увеличение возраста (increase_age)
# class Person:
#     def __init__(self, name, surname, age, sex):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.sex = sex
#
#     def __str__(self):
#         # return self.name
#         return f"{self.name} {self.surname}, {self.age}, {self.sex}"
#
#     def __repr__(self):
#         return f"{self.name} {self.surname}"
#
#     def increase_age(self):             # метод экземпляра класса
#         self.age += 1
#
# person_1 = Person("John", "Wick", 23, "Male")
# print(person_1)
#
# person_1.increase_age()
# print(person_1)



#   смена пола (switch_sex)
class Person:
    def __init__(self, name, surname, age, sex):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.switch_sex() #смена пола всего класса

    def __str__(self):
        # return self.name
        return f"{self.name} {self.surname}, {self.age}, {self.sex}"

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def increase_age(self):
        self.age += 1

    def switch_sex(self):
        sex_dict = {"Male": "Female", "Female": "Male"}
        self.sex = sex_dict[self.sex]

person_1 = Person("John", "Wick", 23, "Male")
print(person_1)

person_1.increase_age()
person_1.switch_sex()
print(person_1)