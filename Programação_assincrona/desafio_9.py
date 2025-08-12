##Monitoramento de download

#Imagine que você está desenvolvendo um gerenciador de downloads que permite baixar múltiplos arquivos simultaneamente. 
# Como nem todos os arquivos têm o mesmo tamanho, alguns downloads demoram mais que outros. Seu programa deve:

#Baixar cinco arquivos diferentes, cada um com um tamanho aleatório entre 10MB e 50MB;
#A velocidade de download de cada arquivo é de 5MB por segundo;
#Exibir mensagens de progresso a cada segundo, mostrando quanto já foi baixado de cada arquivo;
#Exibir uma mensagem quando cada download for concluído;

#Aguarde todos os downloads antes de encerrar o programa.

import asyncio

arquivos = [
    {'nome': 'arquivo_1.txt', 'tamanho': 30},
    {'nome': 'arquivo_2.txt', 'tamanho': 45},
    {'nome': 'arquivo_3.txt', 'tamanho': 20},
    {'nome': 'arquivo_4.txt', 'tamanho': 10},
    {'nome': 'arquivo_5.txt', 'tamanho': 50}
]

async def baixar_arquivo(nome, tamanho, velocidade=5, tempo = 1):
    print(f"Iniciando download de {nome} (tamanho: {tamanho}MB)")
    baixado = 0
    while baixado < tamanho:
        await asyncio.sleep(1)
        baixado += velocidade
        if baixado > tamanho:
            baixado = tamanho
        print(f"[{tempo}s] {nome}: {tamanho} MB baixados")
        tempo += 1
    print(f"{nome} concluído!")

async def main():
    tarefas = [
        asyncio.create_task(baixar_arquivo(arquivo['nome'], arquivo['tamanho']))
        for arquivo in arquivos
    ]
    await asyncio.gather(*tarefas)
    print("Todos os downloads foram concluídos!")


asyncio.run(main())