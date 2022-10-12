
'''
1º- Duck typing, é referente a uma expressão..
"Se anda como pato, faz barulho como um pato, então é um pato" no código isso se
materializa ao você acessar objetos diferentes porém com atributos similares.
Um exemplo seria dois objetos que implementam __getitem__(), no exemplo abaixo usei
a lista padrão e uma class que internamente tem uma tupla, porém como ambos são itéraveis o
mesmo código funciona nos dois. Reutilizando a expressão para esse caso seria: "Se tem __getitem__
então é um iterável".
'''
class SerahQueEhUmaLista:
    def __init__(self):
        self.isso_nao_eh_uma_lista = (1, 2, 3, 4)
    def __getitem__(self, index):
        return self.isso_nao_eh_uma_lista[index]
serah_lista = SerahQueEhUmaLista()
lista = [1, 2, 3, 4]
for item in lista:
    print(item)
for item in serah_lista:
    print(item)
'''
2º - Python data (object) model é devido ao fato de que no python todo tipo de dados são objetos. 
Logo o que diferencia os objetos são seus tipos(classes), que vão indicar se um objeto tem um tipo 
de atributo ou metódo ou não, seus valores e sua identidade id(x).
'''

'''
3º - Dunder methods são os métodos que começam e terminam com dois underlines, um exemplo seria o 
__str___, eles são métodos especiais que geralmente não são invocados diretamente. O exemplo acima 
tem o __getitem__ que fornece um item quando um elemento é iterável, o __str__ é chamado toda vez que 
você chama str(objeto) logo também é chamado quando você faz print(objeto).
'''

'''
4º - Classes abstratas são como se fossem moldes para suas classes filhas, 
eles impedem que você instancie uma classe filha sem implementar os métodos que você queria que 
sejam implementados. São úteis se por exemplo, se você quiser que as classes sempre sejam iteráveis,
 você pode obrigar o usuário a implementar o __getitem__ sempre. Um exemplo onde esse erro acontece é 
 mostrado abaixo.
'''
from collections.abc import Sized
class Teste(Sized):
    def __init__(self):
        self.lista = [1, 2, 3, 4]
teste = Teste()

print(len(teste))
'''
A classe abstrata Sized não permite que você execute o código sem definir o método __len__, 
logo ele nunca chega no print, é uma forma de impedir que erros sejam propagados no seu código. 
Se você corrigir o isso código funcionará.
'''
from collections.abc import Sized
class Teste(Sized):
    def __init__(self):
        self.lista = [1, 2, 3, 4]
    def __len__(self):
        return len(self.lista)
teste = Teste()

print(len(teste))