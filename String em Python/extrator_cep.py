import re

endereco = 'Rua: São Francisco de Assis' \
           'Número: xx' \
           'Cidade: Capelinha' \
           'Cep: 39680-000' \
           'UF: Minas Gerais'

#padrao do cep paraa o re.compile = 5 digitos + hifen opcional + 3 digitos
#uma maneira
#padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')

#usando quantificadores e intervalos
#padrao = re.compile('[0-9]{5}[-]{0,3}[0-9]{3}') < - desta maneira é expecífico
padrao = re.compile('[0-9]{0,5}[-][0-9]{0,5}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(f'Cep: {cep}')