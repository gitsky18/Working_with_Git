def upper_case(string):
    "функция которая делает заглавными первые буквы каждого слова в строке, поступившей на вход функции!!!!!!"
    return string.upper()


import string

def capitalize_words(string):
    "функция которая делает заглавными первые буквы каждого слова в строке,поступившей на вход функции!"
    return ''.join(x.capitalize() for x in string.split())
