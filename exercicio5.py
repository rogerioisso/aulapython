#Ler um valor e escrever se é positivo ou negativo
# (considere o valor zero como positivo), se é par ou ímpar

import unittest




def parimpar(self, numero):
    if (numero % 2) == 0:
        return "Par"
    else:
        return "Impar"

class teste(unittest.TestCase):

    def teste_parimpar(self):
         resultado = parimpar(self, 2)
         self.assertEqual(resultado, "Impar")


unittest.main()


numero = int(input("Digite um numero negativo ou positivo"))



if numero < 0:
    print("Negativo")
    print(parimpar(numero))

elif numero >= 0:
    print("Positivo")
    print(parimpar(numero))

else:
    print("Numero inválido.")


class teste(unittest.TestCase):

    def teste_parimpar(self):

        resultado = parimpar(2)
        self.assertEqual(resultado, "Par")


