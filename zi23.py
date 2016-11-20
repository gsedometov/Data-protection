from argparse import ArgumentParser
from functools import partial
from random import randrange

from utils import add_modulo_256, sub_modulo_256, encode, decode, MAX_VAL

def crypt(msg, key, op):
    return bytes(map(op, msg, key))

def encrypt(args):
    key = generate_key(len(args.m))
    print('Сгенерированный ключ:', decode(key))
    return decode(crypt(encode(args.m), key, add_modulo_256))

def decrypt(args):
    return decode(crypt(encode(args.m), encode(args.k), sub_modulo_256))

def generate_key(l):
	return bytes([randrange(MAX_VAL) for _ in range(l)])

def parse_args():
    parser = ArgumentParser(description='Шифрует и расшифрует строки методом одноразового блокнота.')
    subparsers = parser.add_subparsers()

    enc_parser = subparsers.add_parser('encrypt')
    enc_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    enc_parser.set_defaults(func=partial(encrypt))

    dec_parser = subparsers.add_parser('decrypt')
    dec_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    dec_parser.add_argument('-k', type=str, help='Ключ.')
    dec_parser.set_defaults(func=decrypt)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.func(args))
