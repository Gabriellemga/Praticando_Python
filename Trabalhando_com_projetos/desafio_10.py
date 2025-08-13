## Contador de cédulas únicas

#Um banco está desenvolvendo um sistema para caixas eletrônicos e precisa de um programa que simule o saque de dinheiro. 
#O caixa deve entregar o valor solicitado pelo usuário usando a menor quantidade possível de cédulas. 
#As cédulas disponíveis são: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 2.
#Crie um programa que solicite ao usuário o valor do saque e calcule quantas cédulas de cada tipo serão necessárias para entregar o valor. 
#O programa deve garantir que o valor solicitado seja válido (múltiplo de 2, já que não há cédulas de R$ 1) e tratar erros de entrada caso não seja digitado um valor numérico válido.

def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {}

    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            valor -= quantidade * cedula

    return resultado

def caixa_eletronico():
    try:
        valor = int(input("Digite o valor do saque: R$ "))
        if valor <= 0:
            print("O valor deve ser maior que zero.")
        elif valor % 2 != 0:
            print("Erro. O saque deve ser múltiplo de 2.")
        else:
            cedulas_necessarias = calcular_cedulas(valor)
            print("\nCédulas necessárias:\n")
            for cedula, quantidade in cedulas_necessarias.items():
                print(f"R$ {cedula}: {quantidade} cédula(s)")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


caixa_eletronico()