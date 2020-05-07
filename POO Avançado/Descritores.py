def main():
    print("\n\033[1;34mDescritores funciona como propiedades mas tendo os metodos __get__()\n"
          "__set__ e __del__, são todos feitos por uma classe especifica com protocolo bem definido\033[m\n\n")

    #call = Property()
    callit = Chama('carlos')
    print(callit.nome)
    callit.nome = "Jhonny"
    print(callit.nome)
    del callit.nome



class Property(object):
    "Essa classe seria como o property" ## --> Documentação do property
    def __get__(self, instance, owner): ## --> owner seria a classe que contem a instancia
        print("Retornando nome")
        return instance._nome

    def __set__(self, instance, value):
        print(f"Foi adicionado {value} no atributo.")
        instance._nome = value

    def __delete__(self, instance):
        print("O valor contido no atributo foi apagado.")
        del instance._nome


class Chama(object):
    def __init__(self, name):
        self._nome = name

    nome = Property()


if __name__ == '__main__':
    main()