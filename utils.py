import re

ENCODING = 'cp866'
MAX_VAL = 0x100

def encode(msg):
    return bytes(msg, ENCODING)

def decode(msg):
    return str(msg, ENCODING)

def add_modulo_256(a, b):
    return (a + b) % 256

def sub_modulo_256(a, b):
    return (a - b) % 256


def ifind(pattern, string):
    return (x.group(0) for x in re.finditer(pattern, string))
