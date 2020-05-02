#mechendo com iteraveis

#temos o ZIP, funciona como uma lista,mas um pouquinho diferente.


list1 = ['Arroz', 'feijão', 'macarrão']
list2 = [10, 5, 4]

a = zip(list1, list2)
print('Aqui podemos usar o dict que aceita qualquer iteravel ou o list que tambem aceita.')
print(f'Exemplo com list: {list(a)}')
b = zip(list1, list2)
print(f'Exemplo com Dict: {dict(b)}')

#Agora temos o Map, que é um pouco limitado, pois ele precisa de uma função

a = map((lambda x: x*10), range(10))
print(list(a))

#Nada nos empede de usar uma função pre-definida.

print('\n\n')


def soma(x,y):
    return x + y


l1 = map(soma, range(4), range(3, -1, -1))
print(list(l1))

#Temos tambem o filter que tambem é um pouco limitado, porem tem mais versatilidade e algumas coisas
# a mais que o map e o zip tem.

#Temos um exemplo de pegar apenas valores pares, coisa que o map não faz

l2 = filter((lambda x: x%2 == 0), range(5))
print(list(l2))

#/nada nos empede de de juntar o map com o filter.

a = map((lambda x: x+10), filter((lambda x: x % 2 == 0), range(5)))
print(list(a))

print(f'Seria a mesma coisa com compressão de lista:  {[x+10 for x in range(5) if x%2==0]}')
