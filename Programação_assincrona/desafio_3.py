## Executando fatorial em paralelo

#Carlos precisa calcular o fatorial de cinco números diferentes simultaneamente. 
# Como cálculos pesados podem demorar, ele quer garantir que todos sejam processados ao mesmo tempo, 
# e os resultados exibidos assim que estiverem prontos.Crie um programa que calcule o fatorial de cinco 
# números diferentes de forma assíncrona, onde os cálculos devem ser realizados paralelamente e exiba os resultados conforme forem concluídos, em ordem de menor número para maior número.

import asyncio
import math

numeros = [5, 3, 7, 4, 5, 6]

async def fatorial(numero):
    print(f'-> Calculando o fatorial do {numero}.')
    await asyncio.sleep(3)
    print(f'O fatorial de {numero} é {math.factorial(numero)}\n.')

async def main():
    for n in sorted(numeros):
     await fatorial(n)

asyncio.run(main())



   
