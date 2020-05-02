from os import system

win = ['python randomm.py > dados.txt', 'python arruma.py < dados.txt', 'python arruma.py < dados.txt | python maior.py']

system(win[0])

system(win[1])

system(win[2])
