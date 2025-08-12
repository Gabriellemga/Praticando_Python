## Simulação de sensores ambientais

# Lucas está desenvolvendo um sistema de monitoramento ambiental. Para isso, ele precisa criar sensores assíncronos 
# que coletam dados periodicamente, sem que o programa fique travado esperando por cada um.
# O sistema deve ter três sensores, que coletam e exibem dados em intervalos diferentes:

#Sensor de temperatura: Atualiza os dados a cada 2 segundos.
#Sensor de umidade: Atualiza os dados a cada 3 segundos.
#Sensor de qualidade do ar: Atualiza os dados a cada 5 segundos.
#O sistema nunca deve parar de rodar, exibindo os valores atualizados de cada sensor assim que novos dados estiverem disponíveis.

import asyncio
import random

qualidade_do_ar = ['Ruim', 'Regular', 'Boa', 'Moderada']

async def temperatura():
    tempo = 2
    while True:
        asyncio.sleep(tempo)
        print(f'[{tempo}s] Temperatura: {random.randint(20, 30)} °C')
        tempo += 2 

async def umidade():
    tempo = 3
    while True:
        asyncio.sleep(tempo)
        print(f'[{tempo}s] Umidade: {random.randint(50, 70)} %')
        tempo += 3

async def qualidade_ar():
    tempo = 5
    while True:
        asyncio.sleep(tempo)
        print(f'[{tempo}s] Qualidade do ar: {random.choice(qualidade_do_ar)}')
        tempo += 5

async def main():
    asyncio.gather(temperatura(), umidade(), qualidade_ar())


asyncio.run(main())




