print('Nessa aula vemos como vamos pegar argumentos do terminal com o modulo sys')

import sys

print('\nNo modulo sys temos o argv que basicamente pega os argumentos pasado no propt quando vamos executar um programa')
print(sys.argv)
print('O sys.argv mantem um registro de todos argumentos colocado no prompt')

print('\nVeja um exemplo para ler o arquivo passado no primeiro argumento do prompt.\n')


def main(text, numlines=15):
    lines = text.splitlines()

    while lines:
        read = lines[:numlines]
        lines = lines[numlines:]
        for c in read: print(c)
        if lines and input('More?').upper() is not 'S': break


"""if __name__ == '__main__':
    txt, numlines = None, 5
    if len(sys.argv) > 1:
        txt = open(sys.argv[1]).read()
    if len(sys.argv) > 2:
        try:
            valor = int(sys.argv[2])
        except:
            print('Por favor digite apenas valores inteiros.')
        else:
            numlines = valor

    main(txt, numlines)
"""

print('\nAgora vamos ver como fazer isso com o index: int(sys.argv[sys.argv.index("-l") + 1])')

if __name__ == '__main__':
    txt, numlines = None, 5
    if len(sys.argv) > 1:
        txt = open(sys.argv[1]).read()
    if '-l' in sys.argv:
        try:
            valor = int(sys.argv[sys.argv.index('-l') + 1])
        except:
            print('Por favor digite apenas valores inteiros.')
        else:
            numlines = valor

    main(txt, numlines)