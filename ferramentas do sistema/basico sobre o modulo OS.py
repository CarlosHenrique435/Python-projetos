import os, sys


print('\033[1;30mPara pegar o ID do processo do seu programa ou o  caminho do diretorio do seu programa temos as funções:'
      'os.getpid() e os.getcwd()')

print('\nos.getpid() --> \033[1;31m obetenha(get), id do processo(pid)')
print('\033[1;30mos.getcwd() --> \033[1;31mobtenha o diretorio de trabalho corrente(cwd)\n')

print('\033[1;35m=============================================================\033[1;30m')
print(os.getpid(), os.getcwd())
print('\033[1;35m=============================================================\033[1;30m')

print('\n\033[1;30mPodemos mudar nomes de arquivos com a função os.rename(): Que recebera a instensão(direcionamento)'
      ' do arquivo e o novo nome dele.')
try:
      os.rename('hello', 'ola')
      print('\033[1;35mArquivo renomeado com sucesso.\033[1;30m')
except FileNotFoundError:
      print('\033[1;31mNome de arquivo não encontrado.\033[1;30m')

print('\nPodemos remover arquivos com a função os.remove(diretorio)')
try:
      os.remove('ola')
      print('\n\033[1;35mArquivo removido com sucesso.\033[1;30m')
except FileNotFoundError:
      print('\n\033[1;31mArquivo não encontrado\033[1;30m')

print('\nTemos tambem a função os.urandom(n) que gera n de strings criptocrafadas')

print(os.urandom(10), '<-- \033[1;34m10 Bytes nessa string\033[1;30m')

print('\n\033[1;34m==================================\033[1;30m')
print('Constantes especiais para diretorios')
print('\033[1;34m===================================\033[1;30m')

print('\n\033[1;32mos.pathsep --> saparadpr de caminhos\nos.sep --> separador de diretorio\n'
      'os.pardir --> volta para o diretorio pai(um antes)\n'
      'os.curdir --> pasta atual\nos.linesep --> separação de linha\033[1;30m')

x = os.pathsep, os.sep, os.pardir, os.curdir, os.linesep

print(f'são eles: {x}')

print('\nTemos tambem a função os.environ() que faz um dicionario com as funçoes do sistema')
print(list(os.environ.keys()))

print('\n\033[1;35mPodemos pegar tudo sobre o sistema, como por exemplo o username do meu sistema:\033[1;30m', end=' ')
print(os.environ["USERNAME"])

print('\nVocê pode modificar seu nome tambem (apenas no programa, não muda permanente)')
os.environ["USERNAME"] = 'Carl'
print(os.environ["USERNAME"])