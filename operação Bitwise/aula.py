#Numeros operação Bitwise
#Veromos a função bin(), oct()e, hex() e int()

print(bin(12)[2:])
#bin() --> pega um valor inteiro e converte para binario

#Assim podemos converter de volta com o int
#Na função int temos um argumento pre-definido que seria a base.
print(f'1100 = dec {int("1100", 2)}')

#Tambem temos a função hex() para converter para hexadecimal
print(f'12 = hex {hex(12)[2:]}')
print(f'{hex(12)[2:]} = dec {int("c", 16)}')

#oct() -->  valores octal
print(f'12 --> oct {oct(12)[2:]}')

#SHIFT LEFT(<<) --> Move um determinado valor para a esquerda
#exemplo: 0b000001 << 2 ou 1 << 2 resultado: 0b000100 = 4

#SHI RIGHT(>>) --> manda para direita
#exemplo --> 0b0010100 >> 3 or 20 >> 3 ==> 0b000010 --> 2
#Move o valor 1 3 casas
"""=============================================================================="""
#BIT and = &
# 1 para True e 0 para False

#Exemplo:

#A:  0b00101001
#      ^^^^^^^^
#  &   ||||||||       ->> ira verificar 1 a 1 ficando com o resultado --> 00101001
#B:  0b00101101
#=============================
      #00101001 --> RESULTADO DA OPERAÇÃO
print(int(0b00101001 & 0b00101101))
print(int('00101001', 2))
"""=============================================================================="""
#BIT OR = |
# 1 | 1 = True
# 1 | 0 = True
# 0 | 0 = False

#FAZENDO UM COMPARAÇÃO TEMOS:

#A 0b00100101
#    ^^^^^^^^ --> Fazendo a comparação  A | B ==> 0b00100111
#    ||||||||
#B 0b00100111
#======================
#  0b00100111

print(int(0b00100101 | 0b00100111))
print(int('00100111', 2))
"""===================================================================================="""
#BUT XOR = ^
#Com o XOR é um pouco diferente.
#ele paga o primeiro valor e soma com o segundo(outra comparação) e tiramos o resta da divisão para obter o bit
# 1 ^ 1 = 0 why: 1+1 = 2%2 = 0
# 1 ^ 0 = 1 why: 1+0 = 1%2 = 1

#Fazendo a operação com A e B temos:

#A 0b0101001
#    ^^^^^^^ --> faz a comparação somando e pegando o resta da divisão por 2
#B 0b0010111
#===========================
#  0b0111110

print(int(0b0101001 ^ 0b0010111), int('0b0111110', 2))

# A Criptografia XOR é a unica irreversivel
#Você pode pegar o valor do sesultado e fazer um XOR com o valor B que dara o resultado de A