contatos_lista = [('Elimar', '1234-5678'), ('Thayslane', '44444444'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]

#PASSA UMA LISTA PARA O CONSTRUTOR DO DICIONARIO
contatos = dict(contatos_lista)
print(contatos)

'''
DICIONARIO SAIDA:
{
    'Elimar': '1234-5678', 
    'Thayslane': '9999-9999', 
    'Ana': '8765-4321', 
    'Marina': '8877-7788'
}

'''
print(f' Contato do Elimar: {contatos.get("Elimar", "Contato inexistente!")} ')
#saida caso encontre:  Contato : 1234-5678
#caso contrario: Contato inexistente!


print('Thayslane' in contatos)
#o in, usado dessa forma, verifica apenas as CHAVES do dicionário, não os valores.
#saida: True



#ADICIONANDO NOVOS VALORES
#ADICIONANDO JOAO AO DICIONARIO

contatos['João'] = 55553636

print(contatos)
#saida
'''
{
    'Elimar': '1234-5678', 
    'Thayslane': '9999-9999', 
    'Ana': '8765-4321', 
    'Marina': '8877-7788', 
    'João': 55553636
}
'''

#Removendo itens do dicionário

del contatos['Ana']
print(contatos)
#saida
'''

{
    'Elimar': '1234-5678', 
    'Thayslane': '9999-9999', 
    'Marina': '8877-7788', 
    'João': 55553636
}

'''

#adicionando o 9 na frente dos numeros
novos_contatos = {nome: '9 ' +str(contatos[nome]) for nome in contatos}
print(novos_contatos)

#saida
'''
{
    'Elimar':     '9 1234-5678', 
    'Thayslane':  '9 44444444', 
    'Marina':     '9 8877-7788', 
    'João':       '9 55553636'
}

'''