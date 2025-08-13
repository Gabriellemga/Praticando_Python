## Contagem de vogais em um texto

#Mariana é professora de língua portuguesa e quer um programa que conte quantas vogais há em um texto digitado pelos 
# alunos. Isso ajudará a analisar a estrutura das palavras utilizadas.Crie um programa que peça um texto e exiba quantas 
# vogais (a, e, i, o, u) ele contém.


import unidecode

vogais = ['a','e','i','o','u']
texto = input('Digite o texto: ')

def limpar_texto(texto):
  texto_minusculo = texto.lower()
  texto_sem_acento = unidecode.unidecode(texto_minusculo)
  return list(texto_sem_acento)

def contar_vogais(texto):
  letras= []
  for letra in limpar_texto(texto):
    if letra in vogais:
      letras.append(letra)
  return len(letras)

print(contar_vogais(texto))