#pipes --> seria caminhos de arquivo para arquivo assim como < da aula de streams veja:

from os import system


win = ['type output.py', 'type input.py', 'python output.py', 'python output.py | python input.py']

print('\033[1;34mLendo a saida do arquivo output.py\033[1;30m')
system(win[0])

print('\n\033[1;34mLendo o arquivo input.py\033[1;30m')
system(win[1])

print('\033[1;33m\nExecutando o arquivo output.py.\033[1;30m')
system(win[2])

print('\n\033[1;33mFazendo da saida do output.py um input para o arquivo input.py\033[1;32m\n')
system(win[3])

print('\n\n\033[1;31mPipes podemos usar em qualquer arquivo que temos um input')
