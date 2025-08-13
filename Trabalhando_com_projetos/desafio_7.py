##Jogo de adivinhar o número

#Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. 
#Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.
#Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.
#Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. 
#O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada .

import random

print('Tente advinhar o número (1-100)')

def adivinhar_numero():
  numero_secreto = random.randint(1,100)
  tentativas = 1

  while True:
    try:
       chute = int(input('Digite um número entre 1 e 100 '))
       if chute <= 0 and chute > 100:
        print('Entrada inválida: Número fora do intervalo! Digite um número entre 1 e 100.')
       elif chute < numero_secreto:
          print("Muito baixo! Tente novamente.")
       elif chute > numero_secreto:
          print("Muito alto! Tente novamente.")
       else:
          print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
          break
       tentativas += 1
    except ValueError as e:
        print(f"Entrada inválida: {e}")


adivinhar_numero()
