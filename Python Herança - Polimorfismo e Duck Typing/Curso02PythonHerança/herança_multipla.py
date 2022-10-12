class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def registra_horas(self):
        print('horas registradas - Class Funcionario')

    def mostra_tarefas(self):
        print('fez muita cosia - Class Funcionário')


##########################################dd#
##############################################

class Caelum(Funcionario):
    def mostra_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_curso_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'mostrando curSos ELSE')

###########################################
###########################################

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa ALURETE - class alura')

    def busca_perguntas_sem_respostas(self):
        print('mostrando perguntas  nao respondidas - CLASS ALURA')


###########################################
###########################################

class hipster:
    def __str__(self):
        return f'Hipster {self.nome}'



###########################################
###########################################

class Junior(Alura,hipster):
    pass


###########################################
###########################################

class Pleno(Alura, Caelum, hipster):
    pass


###########################################
###########################################


print('JUNIOR')
elimar = Junior('Elimar')
print(elimar)
elimar.busca_perguntas_sem_respostas()
print('////////////////////')

print('PLENO')
mauro = Pleno('Mauro')
print(mauro)
mauro.busca_perguntas_sem_respostas()
mauro.busca_curso_do_mes()
mauro.mostrar_tarefas()