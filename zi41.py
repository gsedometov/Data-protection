from argparse import ArgumentParser
from functools import partial
from io import StringIO
import re

from utils import encode, decode, ifind

SPACES = [' ', '  '] #['\x20', '\xA0']

def msg2bits(msg):
    ords = map(ord, msg)
    return (int(y) for x in ords for y in bin(x)[2:])

_choose_space = lambda x: SPACES[x]
_join = lambda a, b: ''.join([a, b])

def encrypt_(msg, text):
    words = ifind(r'\w+', text)
    bits = msg2bits(msg)
    spaces = map(_choose_space, bits)
    result = map(_join, words, spaces)
    return ''.join(result) + next(words)

def char_generator(iterable):
    while True:
        ord = next(iterable)
        for _ in range(6):  # По 8 бит на символ
            ord = (ord << 1) + next(iterable)
        yield ord

def decrypt_(text):
    spaces = ifind(r'\s+', text)
    bits = (SPACES.index(s) for s in spaces)
    ords = char_generator(bits)
    return bytes(ords)

def encrypt(args):
    with open(args.f) as container:
        enc = encrypt_(args.m, container.read())
    with open(args.o, 'w') as out:
        out.write(enc)
    return enc

def decrypt(args):
    with open(args.f) as ifile:
        dec = decrypt_(ifile.read())
    return decode(dec)

def parse_args():
    parser = ArgumentParser(description='Шифрует и расшифрует методом табличной маршрутной перестановки.')
    subparsers = parser.add_subparsers()

    enc_parser = subparsers.add_parser('encrypt')
    enc_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    enc_parser.add_argument('-f', type=str, help='Файл-контейнер.')
    enc_parser.add_argument('-o', type=str, help='Выходной файл')
    enc_parser.set_defaults(func=encrypt)

    dec_parser = subparsers.add_parser('decrypt')
    dec_parser.add_argument('-f', type=str, help='Входной файл')
    dec_parser.set_defaults(func=decrypt)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.func(args))
