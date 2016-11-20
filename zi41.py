from argparse import ArgumentParser
from functools import partial
from io import StringIO
import re

from utils import encode, decode, ifind

SPACES = [' ', '  '] #['\x20', '\xA0']

def msg2bits(msg):
    return (int(y) for x in msg for y in bin(x)[2:])

def encrypt(msg, text):
    word = ifind(r'\w+', text)
    with StringIO() as result:
        print2file = partial(print, file=result, end='', sep='')
        for bit in msg2bits(msg):
            print2file(next(word), SPACES[bit])
        print2file(next(word))
        result.seek(0)
        return result.read()

def char_generator(iterable):
    while True:
        ord = next(iterable)
        for _ in range(6):  # По 7 бит на символ
            ord = (ord << 1) + next(iterable)
        yield ord

def decrypt(text):
    spaces = ifind(r'\s+', text)
    bits = (SPACES.index(s) for s in spaces)
    ords = char_generator(bits)
    return bytes(ords)
