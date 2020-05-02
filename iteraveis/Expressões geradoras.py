#oque é um Expressão geradora:


l1 = [c for c in range(10) if c % 2 == 0]

print(l1)

"""
Uma expressão geradora é usada com (parenteses) e não fica gravada na memoria como uma compressão de lista.

compressão de lista --> não tem o obejto iterador ela é apenas iteravel

Enquanto Expressões possui objeto iterador(sendo assim Expressões geradoras não fica guardada na sua memoria, economizando 
espaço na sua RAM)


Uma vez percorrida por um for looping não poderas ser mais percorrida novamente.
"""

E1 = (c**2 for c in range(10) if c % 2 == 0)

for c in E1:
    print(c)

#Percorrida uma vez ela n tera mais utilidade

try:
    print(E1.__next__())
except:
    print('Não percorrida')

print('\n\n')

#Exercicio

word = input('Escreva a sua palavra: ')
l = []

for c in range(len(word)):
    a = word[c:] + word[:c]
    l.append(a)

print(l)

#com Expressão

e = (word[c:] + word[:c] for c in range(len(word)))
for c in e:
    print(c, end='...')
