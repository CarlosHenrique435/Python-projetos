print('\nUsaremos o modulo os para manipulamento')
import os

print('\Para pegar o diretorio em que estamos usamos o os.getcwd()')
print(os.getcwd())

print('Para voltar para o diretorio pai usamos o os.chdir("..") --> chenge directory')
os.chdir('..')

print('\nPara criar diretorios usamos o mkdir()')
os.mkdir('test')
print('criado!')

print('Para ver se o diretorio existe usamos a função os.path.exist("NAME")')
print(os.path.exists('test'))

print('\nPodemos remover um firetorio usando a função os.rmdir()')
os.rmdir('test')
print('removido')

print('Para listar um determinado diretorio usamos o lisdir()')
print(os.listdir(os.getcwd()))

print('\nPara mostrar tudo que ha dentro de diretorios usamos o os.walk() --> seria uma função geradora que devolve\n'
      'o nome, as subs pastas e os arquivos.')

for (name, sub, arq) in os.walk('.'):
    print(f'diretorio ["{name}]"')
    try:
        input('More...')
    except EOFError:
        break
    for fname in arq:
        print(f'--> {os.path.join(name, fname)}')
