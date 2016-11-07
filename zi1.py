from argparse import ArgumentParser
from random import choice
from string import ascii_letters, digits

ALPHABET = ascii_letters + digits

def generate_password(pwd_len):
    return ''.join([choice(ALPHABET) for i in range(pwd_len)])

def encrypt(pwd, bias=2):
    idxs = ((ALPHABET.index(c) + bias) % len(ALPHABET) for c in pwd)
    return ''.join((ALPHABET[i] for i in idxs))

def parse_args():
    parser = ArgumentParser(description='Генерация паролей заданной длины.')
    parser.add_argument('-l', type=int, help='Длина паролей.')
    parser.add_argument('-n', type=int, help='Количество паролей.')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()
    pwds = [generate_password(args.l) for _ in range(args.n)]
    print('Сгенерированные пароли:', *pwds, sep='\n')
    with open('passwords.txt', 'w') as output:
        encrypted = (encrypt(p) for p in pwds)
        print(*encrypted, sep='\n', file=output)
