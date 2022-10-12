from collections.abc import MutableSequence

class Minha_lista_mutavel(MutableSequence):
    pass
 
#leia os erros em tempo de execução
minha_lista = Minha_lista_mutavel()

'''
TypeError: Can't instantiate abstract class Minha_lista_mutavel 
with abstract methods 
__delitem__, 
__getitem__, 
__len__, 
__setitem__, 
insert

'''


