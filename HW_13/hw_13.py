# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат.
# и возвращает список не повторяющихся цитат. Если автор не указан, цитату не брать.
#
#
# 2. Написать функцию, которая принимает результат предыдущей функции и сохраняет в csv файл.
# Имя файла сделать параметром по умолчанию.
# Заголовки csv файла:
# Author, Quote, URL.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).

import requests
import random
import csv


def get_raw_quote(lang="ru"):
    url = "https://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "lang": lang,
              "key": random.randint(1, 999999),
              "qutoteAuthor": True
    }
    response = requests.get(url, params=params)
    return response.json()


def amount_of_quotes(amount):
    quotes = []
    count = 0

    while count < amount:
        quote = get_raw_quote()

        if "quoteAuthor" in quote and quote.get("quoteAuthor"):
            quotes.append(quote)
            count += 1

    return quotes


filename = "file.csv"
data = amount_of_quotes(15)


def write_dict_to_csv(filename, data):
    fieldnames = ["Author", "Quote", "URL"]

    field_correspondence = {"quoteAuthor": "Author", "quoteText": "Quote", "quoteLink": "URL"}

    parsed_data = list()

    for row in data:
        parsed_row = dict()

        for key, value in row.items():
            if key not in field_correspondence:
                continue
            parsed_row[field_correspondence[key]] = value
        parsed_data.append(parsed_row)

    parsed_data = sorted(parsed_data, key=lambda x: x.get("Author").casefold())

    with open(filename, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(parsed_data)


write_dict_to_csv(filename, data)

