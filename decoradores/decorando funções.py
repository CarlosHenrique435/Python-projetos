"""
Funçoes decoradoras evoluem outras fuções e aprimora seus comportamentos
Contendo sua sintaxe propia usando "@" Sintact sugar --> Açucar sintatico
"""
#Exemplo sem "syntact sugar"
#Decorator



"""
                   NÃO RECOMENDADA!!!
"""
def receive(function):
    def Decora():
        print("È um prazer te conhecer!!!")
        function()
        print("Seja bem vindo amigo!!")
    return Decora # Retorna a instancia da função


def Send():
    print("Meu nome é Carlos Henrique")


test = receive(Send)
test()


"""
Utilizando uma sintaxe mais facil para visualização e a mais certa
"""

#Usndo a sintaxe sugar


def receive(function):
    def new_function():
        print("Ola, se apresente, por favor!!")
        function()
        print("Seja bem vindo!!")
    return new_function


@receive #Ele executa a mesma sintaxe do exemplo assima sem a sintaxe sugar
def Send():
    print("Meu nome é Carlos Henrique")


Send()


"""
Podemos usar os decoradores passando argumentos para decorar
"""
print('\n\n')


def Type_tag(type):
    def Getfunc(function):
        def nucleo(n1, n2):
            return f"<{type}>resultado: {function(n1,n2)}</{type}>"
        return nucleo
    return Getfunc


@Type_tag('p')
def soma(n1,n2):
    return f"Soma de {n1} e {n2} é {n1+n2}"


print(soma(5, 10))