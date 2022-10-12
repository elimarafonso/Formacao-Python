class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property #este é o Get_likes
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def dar_likes(self):
        self._likes += 1

    def __str__(self):
        return f'Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}'

######################d######################################
############################################################


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return f'Filme: {self._nome} - Ano: {self.ano} - Duração: {self.duracao}min. - Likes: {self._likes}'

############################################################
############################################################


class Serie(Programa):
    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada


    def __str__(self):
        return f'Serie: {self._nome} - Ano: {self.ano} - {self.temporada} Temporadas - Likes: {self._likes}'

############################################################
############################################################

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #para tornar a classe ITERAVEL
    def __getitem__(self, item):
        return self._programas[item]


    #Para conseguir utilizar a function len()
    '''Desta forma, você consegue chamar len(minha_playlist), já que Playlist implementa __len__. 
        Isso torna a Playlist um Sized (alguém que implementa __len__).'''
    def __len__(self):
        return len(self._programas)


#Com a implementação acima, não precisamos criar estes metodos
'''
@property
 def listagem(self):
     return self._programas

 @property
 def tamanho(self):
     return len(self._programas)
'''



############################################################
############################################################

vingadores = Filme('vingadores - guerra infinita', 2008, 160)
super_man = Serie('super man - a verdadeira história', 2020, 5)
volta_dos_que_não_foram = Filme('Foram e não voltaram 2', 1990, 100)
batman = Serie('O cavaleiro branco', 2002, 3)
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()

super_man.dar_likes()
super_man.dar_likes()

volta_dos_que_não_foram.dar_likes()
volta_dos_que_não_foram.dar_likes()
volta_dos_que_não_foram.dar_likes()

batman.dar_likes()

play_list = [vingadores, super_man, batman, volta_dos_que_não_foram]

playlist_fim_de_semana = Playlist("corujão", play_list)

print(f' Tamanho: {len(playlist_fim_de_semana)}')
for programa in playlist_fim_de_semana:
    print(programa)













