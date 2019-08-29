#Faça um programa que receba um valor que é o valor pago,
# um segundo valor que é o preço do produto e retorne o troco a ser dado.
# (modifique para receber um valor de desconto e subtraia do valor do produto)


class produto:

    def desconto1(valor, desconto, valorpago):

        valor = valorpago-(valor-desconto)

        return valor

    def total(valor, valorpago):
        return valor%valorpago


sc1 = produto
valor = float(input("Digite o valor a ser pago"))
valorpago = float(input("Digite o valor pago"))
op = int(input("Deseja dar um desconto para o cliente? 1 para Sim, 2 para Não"))

if op == 1:
    desconto = float(input("Digite o valor do desconto"))
    print("Troco: {}" .format(sc1.desconto1(valor, desconto, valorpago)))




elif op == 2:
    print("Troco: {}" .format(sc1.total(valor, valorpago)))