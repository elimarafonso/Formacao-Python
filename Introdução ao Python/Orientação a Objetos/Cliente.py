class Cliente:

    def __init__(self, nome = "elimar afonso"):
        self.__nome = nome

    @property
    def nome(self):
        print("entrando no Getter nome.titler()")
        return  self.__nome.title()
    '''  Agora, quando digitarmos nos console "cliente.nome",
         sem a adição dos parênteses, e conseguiremos que o método 
         seja executado como antes. '''

    @nome.setter
    def nome(self, nome):
        print("entrando no Setter nome")
        self.__nome = nome