#all, any, sum e reduce

#all -> Verifica se em uma lista todos os valores são verdadeiros.


print(all([1,2,3,0]))

#any -> verifica se pelo menos algum é verdadeiro

print(any([1,1,1,0,1]))

#sum -> soma os valors de um listas (apenas números)


print(sum([4,3,6,7]))

#reduce -> vem do metodo functools ele basicamente pega os 2 primeiro elemento da sua lista e joga na função
#dps pega um outro elemento da função e soma com a soma dos 2 anterior
import functools


def soma_valores(x,y):
    print(f'adicionando {x} a {y}')
    return x + y


print(functools.reduce(soma_valores, [1,2,3,4,5]))

#como o reduce trabalha por tras dos panos


"""
def reduce(funtion, iterable, ini=None):

    trans = iter(iterable)
    if ini is  None:
        value = next(trans)
    else:
        value = ini
    for valor in trans:
        value = funtion(value, valor)
    return value


print(reduce(soma_valores, [1,2,3,4,5]))
"""
