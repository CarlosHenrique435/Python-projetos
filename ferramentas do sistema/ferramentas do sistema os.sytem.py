import os

print('No modulo Os temos a função os.system() --> Basicamente execulta comandos do terminal.\n'
      'Um exemplo rapido, vamos ler um arquivo pelo os.system().')
os.system('type teste1.txt')
print('\nos.system("type teste1.txt")')

print('\n temos o os.popen() --> funciona como o os.system() porem ele é colocado em um objeto.')

print(os.popen('type teste1.txt'))
print('\nPara ler esse arquivo usamos o .read')
print(os.popen('type teste1.txt').read())

print('\nPor ultimo temos o startfile(Apenas para windows) --> Ele abre um determinado arquivo com o aplicativo padrão'
      'de execusão')

"""import sys

if 'win' in sys.platform:
    os.startfile('teste1.txt')"""


def muda():
      name = input('Digite o nome da pasta para mudar: ')
      print(os.system(f'copy "ferramentas do sistema os.sytem.py" C:\\Users\\carlo\\PycharmProjects\\"retomando tudo\\{name}"'))


muda()
