import random
import string

print('*** GERADOR DE SENHA ***\n' )

def gerar_senha(digitos):
  try:
    if digitos < 12 or digitos > 16:
      print('Erro. A senha deve conter no minimo 12 e no máximo 16 digitos.')
    else:
      caractere = random.choices(string.punctuation)[0]
      letra_maiuscula = random.choices(string.ascii_uppercase)[0]
      letra_minuscula = random.choices(string.ascii_lowercase)[0]
      numeros = random.choices(string.digits)[0]

      todos_digitos = string.punctuation + string.ascii_uppercase + string.ascii_lowercase + string.digits
      digitos_obrigatorios = [caractere, letra_maiuscula, letra_minuscula, numeros]

      senha = []

      senha.extend(digitos_obrigatorios)
      senha.extend(random.choices(todos_digitos, k = digitos - 4))
      random.shuffle(senha)

      print(f'Senha gerada: {"".join(senha)}')
      
  except ValueError:
    print('Os valor deve ser numeros')

while True:
  try:
    print('Insira o numero de digitos entre 12 e 16')
    digitos = int(input('->  '))
    break
  except ValueError:
    print('Entrada inválida. Por favor, insira um número inteiro.')


gerar_senha(digitos)
