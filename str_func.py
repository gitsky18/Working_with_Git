def upper_case(string):
    "функция на вход строку и возвращает ее со всеми заглавными буквами"
    return string.upper()


import string

def capitalize_words(string):
    "функция которая делает заглавными первые буквы каждого слова в строке,поступившей на вход функции"
    return ''.join(x.capitalize() for x in string.split())