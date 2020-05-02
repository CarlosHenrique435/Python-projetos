#Vamos fazer com que os arquivos do diretorio change volta para a pasta que vamos criar.
import os


def NewDir():
    if not os.path.exists('Backup'):
        os.mkdir('Backup')
    arruma('Backup')


def arruma(Name: str):
    os.chdir('change')

    arquivos = None
    for name, sub, arqs in os.walk('.'):
        arquivos = arqs

    for value, arq in enumerate(arquivos):
        os.rename(os.path.join(os.getcwd(), arq), f'Arquivo{value}.txt')

    os.chdir('..')
    for c in arquivos:
        velho = os.path.join('change', c)
        new = os.path.join(Name, c)
        """
        Vemos que os.rename faz papel do mover
        """
        os.rename(velho, new)
        print(f'\033[1;30mMoveu\033[m {velho} \033[1;30mpara\033[m {new}')


if __name__ == '__main__':
    NewDir()
