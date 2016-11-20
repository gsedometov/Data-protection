from argparse import ArgumentParser
from itertools import chain

def encrypt_(msg, key):
    route = chain(*[msg[n::key] for n in range(key)])
    return ''.join(route)

encrypt = lambda args: encrypt_(args.m, args.k)

def parse_args():
    parser = ArgumentParser(description='Шифрует и расшифрует методом табличной маршрутной перестановки.')
    parser.add_argument('-m', type=str, help='Строка для шифрования.')
    parser.add_argument('-k', type=int, help='Ключ (длина строки).')

    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    print(encrypt(args))
