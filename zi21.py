from argparse import ArgumentParser
from functools import partial

from utils import add_modulo_256, sub_modulo_256, encode, decode

def crypt(msg, bias, op):
    return bytes(map(lambda x: op(x, bias), msg))

def process_io(fun, args):
    return decode(fun(encode(args.m), args.k))

encrypt = lambda args: process_io(partial(crypt, op=add_modulo_256), args)
decrypt = lambda args: process_io(partial(crypt, op=sub_modulo_256), args)

def parse_args():
    parser = ArgumentParser(description='Шифрует и расшифрует строки методом одноалфавитной подстановки.')
    subparsers = parser.add_subparsers()

    enc_parser = subparsers.add_parser('encrypt')
    enc_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    enc_parser.add_argument('-k', type=int, help='Ключ (смещение).')
    enc_parser.set_defaults(func=encrypt)

    dec_parser = subparsers.add_parser('decrypt')
    dec_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    dec_parser.add_argument('-k', type=int, help='Ключ (смещение).')
    dec_parser.set_defaults(func=decrypt)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.func(args))
