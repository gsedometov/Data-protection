from argparse import ArgumentParser
from itertools import chain, zip_longest
from functools import partial
from operator import ne

from utils import partitions

def encrypt_(msg, key):
    parts = partitions(msg, key)
    route = chain(*zip_longest(*parts))
    route = filter(partial(ne, None), route)
    return list(route)

def decrypt_(msg, key):
    excess = key - (len(msg) % key)
    msg = chain(msg, '\xA0' * excess)
    drop_pads = partial(ne, '\x32')
    decrypted_block = encrypt_(msg, key)
    result = filter(drop_pads, decrypted_block)
    return list(result)

encrypt = lambda args: ''.join(encrypt_(args.m, args.k))
decrypt = lambda args: ''.join(decrypt_(args.m, args.k))

def parse_args():
    parser = ArgumentParser(description='Шифрует и расшифрует методом табличной маршрутной перестановки.')
    subparsers = parser.add_subparsers()

    enc_parser = subparsers.add_parser('encrypt')
    enc_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    enc_parser.add_argument('-k', type=int, help='Ключ.')
    enc_parser.set_defaults(func=encrypt)

    dec_parser = subparsers.add_parser('decrypt')
    dec_parser.add_argument('-m', type=str, help='Строка для шифрования.')
    dec_parser.add_argument('-k', type=int, help='Ключ.')
    dec_parser.set_defaults(func=decrypt)

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(args.func(args))
