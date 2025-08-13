##Calculando a gorjeta em um restaurante

#João trabalha como garçom em um restaurante e precisa calcular a gorjeta que os clientes deixam ao pagar a conta. 
# O restaurante sugere uma gorjeta de 10%, mas alguns clientes podem escolher dar mais ou menos.
# Para agilizar o processo, João quer um programa que receba o valor total da conta e a porcentagem de gorjeta desejada e exiba o valor final que o cliente deverá pagar.
# Crie um programa que peça ao usuário o valor da conta e a porcentagem de gorjeta.
#  O programa deve calcular e exibir o valor da gorjeta e o total a ser pago.


conta = float(input('Digite o valor da conta:' ))
gorjeta = float(input('Digite o valor em porcetagem da gorjeta: '))

def calcular_gorjeta(conta, gorjeta):
    valor_gorjeta = conta * (gorjeta/100)
    total_pagar = conta + valor_gorjeta
    print(f'Valor da gorjeta: R$ {valor_gorjeta:.2f}')
    print(f'Total a pagar: R$ {total_pagar:.2f}')

calcular_gorjeta(conta, gorjeta)
