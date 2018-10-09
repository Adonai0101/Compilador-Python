import re

def var(cad):
    regex = re.compile('[a-zA-Z]')
    obj = regex.match(cad)
    return bool(obj)

def esNumero(cad):
    regex = re.compile('[0-9]')
    obj = regex.match(cad)
    return bool(obj)