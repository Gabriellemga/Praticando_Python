## Executando duas tarefas ao mesmo tempo

#Carlos é um engenheiro de software que precisa processar duas tarefas simultaneamente: 
#uma que simula um download e outra que simula uma análise de dados. Ele quer que ambas as tarefas sejam 
# iniciadas ao mesmo tempo, e que o programa exiba mensagens informando o início e o fim de cada uma.
#Com base nesse cenário, crie um programa que inicie ambas as tarefas ao mesmo tempo, e exiba
#as mensagens quando cada uma for concluída. Dica: Utilize asyncio.gather() para rodar ambas em paralelo.

import asyncio

async def download():
    print('Iniciando download...')
    await asyncio.sleep(2)
    print('Download concluído.')

async def analise_dados():
    print('Iniciando analise de dados...')
    await asyncio.sleep(2)
    print('Analise de dados concluída.')


async def main():
    await asyncio.gather(download(), analise_dados())

asyncio.run(main())