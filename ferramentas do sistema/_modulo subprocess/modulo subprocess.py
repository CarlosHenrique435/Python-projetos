"""
Processo --> Programa(main)
Modulo subprocess --> Execução de um codigo dentro do processo
"""

import subprocess, os

print('\nNo modulo temos a função call que seria como o os.system')

print('\n\033[1;32mExemplo com call\033[m')
print(subprocess.call(['dir'], shell=True)); """Vemos que colocamos shell como True, isso seria para execultar o argv no shell"""

print('\n\033[1;34mExemplo com system\033[m')
os.system('dir')

print('\nTemos a função check_call --> Que verifica se o comando vai execultar com sucesso')
try:
    print(subprocess.check_call(['type', 'tente.txt'], shell=True))
except subprocess.CalledProcessError:
    print('Esse comando não existe!')

print("\nPodemos armazenar tudo em um variavel usando a função check_output.")
armazena = subprocess.check_output(['type', 'tente.txt'], shell=True)
print(str(armazena))

print('\nPor fim temos o Popen que é semelhante ao do modulo os.')
process = subprocess.Popen(['type', 'tente.txt'], stdout=subprocess.PIPE, shell=True)
print(process.communicate())
print('O None seria o stderr')

print('\n\nPodemos usar o comunicate para mandarmos alguma coisa para outro programa:')

send = subprocess.Popen(['python', 'input.py'], stdin=subprocess.PIPE)
#Agora mandamos em Bytes pelo comunicafe
send.communicate(b'Ola meu nome e carlos')