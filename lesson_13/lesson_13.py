import requests
import random

# url = "https://api.forismatic.com/api/1.0/"
# response = requests.get(url)
# print(response.status_code)
# print(response.text)





# url = "https://api.forismatic.com/api/1.0/"
# params = {"method": "getQuote",
#           "format": "json",
#           "lang": "ru"}
# response = requests.get(url, params=params)
# print(response.status_code)
# print(response.text)


# def get_quote(lang="ru"):
#     url = "https://api.forismatic.com/api/1.0/"
#     params = {"method": "getQuote",
#              "format": "json",
#              "lang": lang}
#     response = requests.get(url, params=params)
#     return response.json()
#
# res = get_quote()
# print(res)




# def get_raw_quote(lang="ru"):
#     url = "https://api.forismatic.com/api/1.0/"
#     params = {"method": "getQuote",
#              "format": "json",
#              "lang": lang,
#               "key": random.randint(1, 999999)}
#     response = requests.get(url, params=params)
#     return response.json()
#
#
# def get_quote(raw_quote):
#     return raw_quote['quoteText']
#
#
# def get_qauthor(raw_quote):
#     return raw_quote['quoteAuthor']
#
#
# for request_number in range(100):
#     raw_quote = get_raw_quote()
#     quote = get_quote(raw_quote)
#     print(quote)
#
# res = get_raw_quote()
# print(res)




def get_raw_quote(lang="ru"):
    url = "https://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
             "format": "json",
             "lang": lang,
              "key": random.randint(1, 999999)}
    response = requests.get(url, params=params)
    return response.json()


def get_quote(raw_quote):
    return raw_quote['quoteText']


def get_qauthor(raw_quote):
    return raw_quote['quoteAuthor']


for request_number in range(100):
    raw_quote = get_raw_quote()
    quote = get_quote(raw_quote)
    print(raw_quote)

res = get_raw_quote()
print(res)
