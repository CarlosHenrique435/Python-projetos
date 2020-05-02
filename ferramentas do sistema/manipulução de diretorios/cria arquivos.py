#Criando arquivos para exercicio.

import os


def main():
    if os.path.exists('chage'):
        os.mkdir('change')
    os.chdir('change')
    print(os.getcwd())
    for c in ('abcd','efgh', 'ijk', 'lmno','pqr', 'uvw', 'xyz'):
        if os.path.exists(c):
            with open(f'{c}.txt','a') as f:
                pass
        else:
            pass


if __name__ == '__main__':
    main()
