# Exercicio 1- Escreva uma classe que contém um método que calcule se a pessoa é maior de 18 anos ou não.
# Receba os dados pela console e chame este método. (modifique este exercício para receber 5 alunos,
# 3 notas para cada um e calcule a média mostrando se está aprovado ou não)

import unittest

class aluno():

    def verificacao(self, n1, n2, n3):
        return (n1+n2+n3)/3




    def veriaprov(media):

        if media > 6 and media <= 10:
            return "aprovado"

        elif media < 6 and media > 0:
            return "reprovado"

        else:
            return "maior/menor que o limite ente 0 a 10"



class TesteAluno(unittest.TestCase):

    def testeverifica(self):
        Aluno = aluno()
        aprovado = Aluno.verificacao(7.3,7.0,6.6)
        self.assertEqual(aprovado, 7)


unittest.main()

func = aluno
aluno_lista = []


for i in range(5):
    nome_aluno = input("Digite o nome do aluno")
    n1 = int(input("Digite a n1"))
    n2 = int(input("Digite a n2"))
    n3 = int(input("Digite a n3"))



    media = func.verificacao(n1,n2,n3)

    aluno_lista.append("Aluno {} com media {} está {} " .format(nome_aluno, func.verificacao(n1, n2, n3), func.veriaprov(media)))

    print("\n\n")
print(aluno_lista)