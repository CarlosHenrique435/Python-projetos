def main():
    print('\n\033[1;35mAprendo Descritores e propiedades com a função property()')
    print("property() --> Permite gerenciar a manipulação de atributos")
    print("Semelhante aos metodos magicos __getattr__ e __setattr__\033[m\n\n")

    call = Exemplo('Carlos')
    print(call.name)
    call.name = "Alisson Silva"
    print(call.name)
    del call.name
    print(Exemplo.name.__doc__)


class Exemplo:
    def __init__(self, name):
        self._name = name #Se usarmos um "_" no começo do atributo indica que ele é uma propiedade

    def getname(self):
        print("Pegando atributos")
        return self._name

    def setname(self, value):
        print(f"Adicionando {value} ao atributo.")
        self._name = value
        print("Adicionado com sucesso!")

    def delItem(self):
        print(f"Apagando o Atributo com valor --> {self._name}")
        del self._name

    name = property(getname, setname, delItem, "Usando property como exemplo __getattribute__")


if __name__ == '__main__':
    main()
