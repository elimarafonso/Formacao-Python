'''Expressões Regulares -> RegEx'''

import re


url_original ='https://www.bytebank.com/cambio'
padrao_de_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_de_url.match(url_original)

if not match:
    raise ValueError('URL FORA DOS PADRÕES !!!!!!!!!!!1')

print('URL válida :-)')




###############################
'''


Expressões Regulares é um tópico muito extenso na área de computação e muito importante. 
Praticamente toda linguagem de programação possui um conjunto de ferramentas para trabalhar com Expressões Regulares.
O mais interessante é que, apesar de serem linguagens diferentes, o modo de utilizar vai ser muito parecido com o que vimos: 
estabelecer um padrão (RegEx) e aplicar esse padrão a um texto, ora para extrair o valor que esteja de acordo com 
o padrão fornecido (search), ora para verificar se o texto está de acordo com o padrão (match).
Se você se interessou pelo assunto e quer se aprofundar ainda mais, a documentação oficial do Python tem 
uma seção de HOWTO (“como fazer”) voltada especificamente em como trabalhar com expressões regulares. Ela pode 
ser acessada através do link: https://docs.python.org/pt-br/3/howto/regex.html#regex-howto

'''