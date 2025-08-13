## Calculadora com tratamento de erros

# Carlos está criando uma calculadora simples, mas quer garantir que o programa não quebre se o usuário digitar valores inválidos, ele precisa tratar os erros.
#Crie uma calculadora que permita ao usuário escolher entre soma, subtração, multiplicação e divisão. Além de modularizar o código em funções, use try-except para tratar erros de entrada inválida, que consiste em:

#Caso digite um caractere em vez de número | exceção a ser lançada: ValueError;
#Caso tente fazer uma divisão por 0 | exceção a ser lançada: ZeroDivisionError.

def somar(numero1,numero2):
  return numero1 + numero2

def subtrair(numero1,numero2):
   return numero1 - numero2

def multiplicar(numero1,numero2):
  return numero1 * numero2

def dividir(numero1,numero2):
  if numero2 == 0:
    print('Erro: Divisão por zero não é permitida.')
  else:
   return numero1 / numero2
 
def calculadora():
  try:
    numero1 = float(input('Digite o primeiro número: '))
    operacao = input('Escolha a operação (+, -, *, /): ')
    numero2 = float(input('Digite o primeiro número: '))   
    if operacao == '+':
      print(f' Resultado: {somar(numero1,numero2)}')
    elif operacao == '-':
      print(f'Resultado: {subtrair(numero1,numero2)}')
    elif operacao == '*':
      print(f'Resultado: {multiplicar(numero1,numero2)}')
    elif operacao == '/':
      print(f'Resultado: {dividir(numero1,numero2 )}')
    else:
      print('Operação invalida.')
  except ValueError:
       print("Erro: Entrada inválida. Digite apenas números.")


calculadora()
