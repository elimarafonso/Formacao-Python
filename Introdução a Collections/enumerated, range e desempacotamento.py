usuarios = [
    ('Elimar afonso', 29, 1993),
    ('Thayslane abrante', 24, 1998),
    ('Maxima damiao de souza', 45, 1978)
]

'''for nome, idade, nascimento in usuarios:
    print(f'Nome: {nome} - Nascimento: {nascimento}')'''

for usuario in enumerate(usuarios):
    print(usuario)
#saida :
'''
(0, ('Elimar afonso', 29, 1993))
(1, ('Thayslane abrante', 24, 1998))
(2, ('Maxima damiao de souza', 45, 1978))
'''