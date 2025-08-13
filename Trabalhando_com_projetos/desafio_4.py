## Identificando palavras mais longas em um texto

#Sofia é revisora de textos e precisa identificar palavras muito longas em um parágrafo. 
#Textos mais fáceis de ler costumam ter palavras curtas, então ela quer um programa que encontre palavras que tenham mais de 10 letras e as exiba em destaque.
#Crie um programa que receba um texto e exiba todas as palavras que possuem mais de 10 letras. 
#Caso nenhuma palavra longa seja encontrada, o programa deve avisar o usuário.

texto = input('Digite o seu texto: ')

def contar_mais_10_letras(texto):
  mais_10_letras = []
  texto = texto.split()
  for palavra in texto:
      if len(palavra) > 10:
        mais_10_letras.append(palavra)

  if mais_10_letras:
    print(f' As palavras que possuem mais de 10 letras são:{", ".join(mais_10_letras)}.')
  else:
    print('Nenhuma palavra foi encontada no texto.')


contar_mais_10_letras(texto)