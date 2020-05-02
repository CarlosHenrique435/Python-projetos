import json

identidade = {'nome': 'carlos', 'idade': 16, 'peso': 70, 'altura': 1.82}
data_string = json.dumps(identidade)

with open('bancoJson.json', 'wb') as file:
    file.write(data_string.encode())


with open('bancoJson.json', 'rb') as file2:
    data1 = file2.readline()
    data = json.loads(data1)
    print(data)



#Com isso podemos fazer com tuplas e listas
#E podemos retornar para um objeto python

