from collections import Counter

def analisa_frequencia_de_letras(texto):
  aparicoes = Counter(texto.lower())
  total_de_caracteres = sum(aparicoes.values())

  proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
  proporcoes = Counter(dict(proporcoes))

  mais_comuns = proporcoes.most_common(10)
  for caractere, proporcao in mais_comuns:
    print("{} => {:.2f}%".format(caractere, proporcao * 100))





texto = '''
ais uma noite como todas as anteriores. Pego minha caneca de café cheia, acendo meu ultimo cigarro e corro pra velha janela do quarto. Observo a noite fria e chuvosa, até parece confortável por um momento, se não fossem as dezenas de preocupações que me desmotivam a cada dia.

Penso em você, mesmo sabendo o quão longe está de mim, sinto aquele amor que continua a me desgraçar intensamente a cada dia, e penso quando enfim poderei te ter comigo. Sei lá, o café chega ao fim e trago a ultima ponta, nada muda. É como se eu fosse passar por isso mais uns longos anos a frente.

Cada vez mais tenho a sensação de incertezas e inseguranças e tento me manter firme apesar disso. Algumas coisas parecem dar certo e maioria não, tipo você.

Então após 10 minutos refletindo, largo tudo, fecho a janela e volto pro meu mundo dentro do quarto. Não sei até quando, não sei o porquê, só sei que tá tudo tão errado e quero me livrar disso o quanto antes. E tu não tem nem ideia do quanto, amor meu. 
'''
analisa_frequencia_de_letras(texto)

'''
saida:
 => 18.47% (espaço)
e => 9.99%
o => 9.28%
a => 9.18%
s => 5.45%
n => 5.15%
t => 4.44%
r => 4.44%
i => 4.24%
m => 4.24%

'''