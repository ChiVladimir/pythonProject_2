#Домашнее задание по теме "Интроспекция"


import sys
from pprint import pprint
import inspect
from textblob import TextBlob
from langdetect import detect

def introspection_info(obj):
    _info = {}
    _info["type"] = type(obj)
    _info["attributes"] = [a for a in dir(obj) if not callable (getattr(obj, a))]
    _info['methods'] = [a for a in dir(obj) if callable (getattr(obj, a))]
    _info["module"] = obj.__class__.__module__
    if isinstance(obj, str):
        _info["add_info"] = f"{obj} is a string is written in the language {detect(obj)}"
    elif isinstance(obj, int):
        if is_prime(obj):
            _info["add_info"] = f"{obj} is a prime number"
        else:
            _info["add_info"] = f"{obj} is not a prime number"
    else:
        _info["add_info"] = f"{obj} is an other object"
    return _info

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":


    number_info = introspection_info(42)
    print(type(inspect.getmodule(number_info)), inspect.getmodule(number_info))
    print(number_info)
    str_info = introspection_info('Gruß')
    print(str_info)
