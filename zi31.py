from argparse import ArgumentParser
from operator import itemgetter

from utils import encode, decode

def encrypt_(msg, key):
    keys = (int(x) for x in key.split())
    result = sorted(zip(msg, keys), key=itemgetter(1))
    return ''.join(next(zip(*result)))

def decrypt_(msg, key):
    keys = (int(x) for x in key.split())
    return ''.join((msg[k] for k in keys))

encrypt = lambda args: encrypt_(args.m, args.k)
decrypt = lambda args: decrypt_(args.m, args.k)

def parse_args():
    parser = ArgumentParser(description='Шифрует и расшифрует методом линейной перестановки')
    subparsers = parser.add_subparsers()

    enc_parser = subparsers.add_parser('encrypt')
    enc_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    enc_parser.add_argument('-k', type=str, help='Ключ.')
    enc_parser.set_defaults(func=encrypt)

    dec_parser = subparsers.add_parser('decrypt')
    dec_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    dec_parser.add_argument('-k', type=str, help='Ключ.')
    dec_parser.set_defaults(func=decrypt)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.func(args))
