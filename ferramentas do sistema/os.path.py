import os


print('\033[1;34mAPRENDENDO UM POUCO SOBRE OS.PATH')

print('\n\033[1;35m==================================================================================================')
print('\033[1;30mTemos a função os.path.isdir("name") -->  Verifica se o argumento passado é um diretorio (True or False)')
print('Temos o os.path.isfile("name") --> Verifica se o argumento(arquivo) passado é um arquivo.')
print('Temos o os.path.exists("name") --> Verifica se existe esse nome no diretorio passado.')
print('Temos o os.path.getsize("name file") --> Retorna o tamanho do arquivo em Bytes')


print("\033[1;34m\nLIDANDO COM NOME DE ARQUIVO OU DIRETORIO")

print('\n\033[1;35m==================================================================================================\033[1;30m')
print('Temos a função os.path.split("dir") --> Verifica o diretorio passado como argumento e separa arquivo de diretorio')
print('Temos a função os.path.join(args) --> recebe argumentos e cria um caminhos com os argumentos passados.')
print('Temos a função os.path.dirname("diretorio") --> Pega o diretorio e devolve apenas o diretorio.')
print('Temos a função os.path.basename("diretorio") --> Verifica seu diretorio e devolve apenas o nome do arquivo')
print('Temos a função os.path.splitext("diretorio or file") --> verifica e sepera instenção de arquiivo')
print(os.path.splitext('basico sobre o modulo OS.py'))
print('Temos a função os.path.normpath("diretorio") --> Verifica o diretorio passado e coloca separadores adapitados para'
      'o seu sistema operacional')


print('\n\033[1;34mE POR ULTIMO TEMOS O OS.PATH.ABSPAYH()')
print('\n\033[1;35m==================================================================================================\033[1;30m')
print('os.path.abspath("") --> Se passado um arg vazio ele devolve o propio caminho que vc esta trabalhando(relativo)')
print(os.path.abspath(''))
print('Quando colocado um nome de um diretorio como argumento ele devolve o caminho absoluto para ate o argumento digitado')
print(os.path.abspath('..\\iteraveis'))


