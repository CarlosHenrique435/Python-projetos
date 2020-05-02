import sys

#plataform --> sys.plataform devolvera o seu sistema operacional(Da maquina que você está usando)

print(sys.platform)
#podemos importar o modulo winsound se o sistema for windows.

if 'win' in sys.platform:
    import winsound
else:
    print('Sua aplicação não terá som, pois você não está em sistema operacional compativel com algumas'
          'bibliotecas')

print('\n')

#Temos o sys.path que retorna a você uma lista de caminhos que é posivel de vc chamar ou achar algun arquivo.
print(sys.path)
      #você pode usar o .append() no path para adicionar mais caminhos que ele possa chamar


#Temos tbm o sys.exit[args] --> tem como objetivo fechar o programa em que está em execução e em args você pode
#colocar um valor interiro que ele ira colocar na tela antes de fechar (usando para verificações de erros).

#Temos o sys.modules --> Irá criar um dicionario com todos os modulos usados em seu programa

print(sys.modules)
#Veja que aparece varios modulos que seu programa precisa, se em um programa mt grande em determinada parte você
#não precisar mais de um modulo você pode retirar ele, isso lhe dará mais eficiencia e seu programa rodará mais leve


#Por fim temos o exec.info() --> ele basicamente mostra um tupla com os argumentos da sua ultima exesão

try:
    import pprin
except:
    print(sys.exc_info())
