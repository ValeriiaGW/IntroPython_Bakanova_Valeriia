# методы словарей

symbols = {symbol: ord(symbol) for symbol in 'eyuioa'}

persons = {"John": 12, "Jack": 34, "Anna": 27}

# print(persons["Anna"])

persons["Jackob"] = 59
persons["John"] = len("Test")
# persons.clear()
# persons = {}
# print(persons.get("Vova", -1))

result = "Anna" in persons  # in проверяет ТОЛЬКО КЛЮЧИ!!

key = "Anna"
# if key not in persons:
#     persons[key] = 41
#
for key in persons:
    print(key, persons[key])
value = persons.pop("Jackob")
print(">>>>>", value)
for key, value in persons.items():
    print(key, value)

# print(type(persons.keys()), persons.keys())
# print(type(persons.values()), persons.values())

max_age = max(persons.values())

# print("\m\\a\\x\_\\a\\g\\e")
#
# value = input()
# print(value)


# persons = {"John": 12, "Jack": 134}
# persons_other = {"Anna": 42, "Jack": 64}
#
#
# persons_result = {}
# persons_result.update(persons)
# persons_result.update(persons_other)
# print(persons_result)
#
# max_age = max(persons_result.values())
# print(max(list(persons.values()) + list(persons_other.values())))

# persons_result = {**persons, **persons_other}
# print(persons_result)

products = [{"name": "water", "price": 12, "title": "Bonaqua"},
            {"name": "bread", "price": 7, "title": "Baton"},
            {"name": "bread", "price": 9, "title": "WhiteBread"},
            {"name": "apple", "price": 25, "title": "Golden"}]

bread_prices = []
for product in products:
    if product["name"] == 'bread':
        # bread_prices.append(product['price'])
        product['price'] = product['price'] * 1.1 - 1
print(products)
