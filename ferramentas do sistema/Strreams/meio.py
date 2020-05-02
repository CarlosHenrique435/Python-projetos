from os import system

win = ['python inter.py', 'type leiame.txt', 'python inter.py < leiame.txt', 'python inter.py < leiame.txt > out.txt']

try:
    system(win[0])
except KeyboardInterrupt:
    print('\nO inter acabou')

try:
    system(win[1])
    print('Fim da leitura.')
except (KeyboardInterrupt):
    print('Fim da leitura.')

try:
    system(win[2])
    """
    Em win[3] Temos um sinal de menor para o inter.py oque significa?:
    Ele basicamente pega o output que esta no leima.txt e passa para o input do inter.py
    """
except (EOFError):
    print('Fim')

try:
    system(win[3])
    """
    Em win[3] Temos um sinal de menor para o inter.py oque significa?:
    Ele basicamente pega o output que esta no leima.txt e passa para o input do inter.py
    """
except (EOFError):
    print('Fim')
