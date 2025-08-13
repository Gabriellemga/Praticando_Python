## Gerador de senha segura

# Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários.
# Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.
#Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. 
#Exiba a senha gerada.

import random
import string


def gerar_senha():
  caractere = random.choices(string.punctuation)[0]
  letra_maiuscula = random.choices(string.ascii_uppercase)[0]
  letra_minuscula = random.choices(string.ascii_lowercase)[0]
  numeros = random.choices(string.digits)[0]

  todos_digitos = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
  digitos_obrigatorios = [caractere, letra_maiuscula, letra_minuscula, numeros]

  senha = []

  senha.extend(digitos_obrigatorios)
  senha.extend(random.choices(todos_digitos, k = 8))
  random.shuffle(senha)

  print(f'Senha gerada: {"".join(senha)}')

gerar_senha()

