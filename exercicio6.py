# Escreva um algoritmo que leia 10 números informados pelo
# usuário e, depois, informe o menor, número, o maior número, a soma dos
# números informados e a média aritmética dos números informados.

import unittest



def menornum(num_lista, aux):
    for i in range(10):
        if num_lista[i] < aux:
            aux = num_lista[i]

    return aux
#verifica o menor numero da lista de numero inseridos pelo usuario

class Teste(unittest.TestCase):

    def teste_menornum(self):

        menor = menornum(num_lista, aux)

        self.assertEqual(menor, 1)
#verifica se o menor numero da lista é 1, se não da erro

num_lista = []

for i in range(10):
    numero = int(input("(posição: {} ) Digite o numero: ".format(i)))
    num_lista.append(numero)

aux = num_lista[0]
unittest.main()
print("Numero menor: ", menornum(num_lista, aux))