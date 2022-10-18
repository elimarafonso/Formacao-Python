class Produto(object):

  def __init__(self, nome, valor):
    self.__nome = nome.upper()
    self.__valor = valor

  def __repr__(self):
    return "nome:%s valor:%s" % (self.__nome, self.__valor)

  def get_nome(self):
    return self.__nome

  def get_valor(self):
    return self.__valor

########################################]



# função sorted()
numeros = [3, 5, 2, 43, 54, 3, 3, 4, 5, 4, 32, 7, 53, 1]
numeros_ordenados = sorted(numeros)

print(numeros)
print(numeros_ordenados)

#########
#Ordenando lista de strings no Python
print('Ordenando lista de strings no Python')
palavras = ["chocolate","biscoito", "cafe", "suco", "feijao", "arroz"]
palavras_ordenadas = sorted(palavras)

print(palavras)
print(palavras_ordenadas)

print('############################')
print('Ordenando lista de objetos no Python')

chocolate = Produto('chocolate', 3.45)
biscoito = Produto('biscoito', 2.49)
cafe = Produto('cafe', 3.45)
suco = Produto('suco', 4.3)
feijao = Produto('feijao', 10.0)
arroz = Produto('arroz', 8.5)

produtos = [chocolate,biscoito,cafe, suco, feijao,arroz]
produtos_ordenados = sorted(produtos, key = Produto.get_valor)
print(f'PRODUTOS ORDENADOS POR VALOR: {produtos_ordenados}')
#saida
'''
PRODUTOS ORDENADOS: 
[
    nome:biscoito valor:2.49, 
    nome:chocolate valor:3.45, 
    nome:cafe valor:3.45, 
    nome:suco valor:4.3, 
    nome:arroz valor:8.5, 
    nome:feijao valor:10.0
]


'''
produtos_ordenados = sorted(produtos, key = Produto.get_nome)
print(f'PRODUTOS ORDENADOS POR NOME: {produtos_ordenados}')
'''
PRODUTOS ORDENADOS POR NOME: 
[
    nome:arroz valor:8.5, 
    nome:biscoito valor:2.49, 
    nome:cafe valor:3.45, 
    nome:chocolate valor:3.45, 
    nome:feijao valor:10.0, 
    nome:suco valor:4.3
]

'''
print('##############################')
print('Realizando ordenação reversa no Python')
produtos_ordenados = sorted(produtos, key = Produto.get_valor, reverse= True)
print(f'PRODUTOS ORDENADOS POR NOME: {produtos_ordenados}')
#saida
'''
PRODUTOS ORDENADOS POR NOME: 
[
    nome:FEIJAO valor:10.0, 
    nome:ARROZ valor:8.5, 
    nome:SUCO valor:4.3, 
    nome:CHOCOLATE valor:3.45, 
    nome:CAFE valor:3.45, 
    nome:BISCOITO valor:2.49]


'''