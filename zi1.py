from random import choice
from string import ascii_letters, digits

ALPHABET = ascii_letters + digits
n_letters = len(ALPHABET)

def generate_password(pwd_len):
    return ''.join([choice(ALPHABET) for i in range(pwd_len)])

def encrypt(pwd, bias=2):
    idxs = ((ALPHABET.index(c) + bias) % n_letters for c in pwd)
    return ''.join((ALPHABET[i] for i in idxs))

if __name__ == '__main__':
    n_pwds = int(input('Введите количество паролей: '))
    pwd_len = int(input('Введите длину пароля: '))
    pwds = [generate_password(pwd_len) for _ in range(n_pwds)]
    print('Сгенерированные пароли:', *pwds, sep='\n')
    with open('passwords.txt', 'w') as output:
        encrypted = (encrypt(p) for p in pwds)
        print(*encrypted, sep='\n', file=output)