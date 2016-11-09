from argparse import ArgumentParser
from operator import add, sub

from codec import encode, decode, MAX_VAL

def crypt(msg, bias, op):
    return bytes([op(m, bias) % MAX_VAL for m in msg])

encrypt = lambda args: crypt(encode(args.m), args.k, add)
decrypt = lambda args: crypt(encode(args.m), args.k, sub)

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
