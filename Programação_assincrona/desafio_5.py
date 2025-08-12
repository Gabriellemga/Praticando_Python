## Processando pedidos de uma loja

# Marcos é dono de uma loja online e precisa de um sistema que processe pedidos de forma assíncrona. 
# O sistema deve seguir a seguinte lógica:

#Primeiro, verificar se o pagamento foi aprovado;
#Se o pagamento for aprovado, verificar se há estoque disponível;
#Somente se houver estoque disponível, confirmar o pedido e enviá-lo para entrega;
#Se o pagamento falhar ou não houver estoque, o pedido deve ser cancelado.

# A lista de pedidos já está definida no sistema, com o status do pagamento e do estoque previamente cadastrados. 

import asyncio

pedidos = [
    {"id": 101, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 102, "pagamento_aprovado": True, "estoque_disponivel": False},
    {"id": 103, "pagamento_aprovado": False, "estoque_disponivel": True},
    {"id": 104, "pagamento_aprovado": True, "estoque_disponivel": True},
    {"id": 105, "pagamento_aprovado": False, "estoque_disponivel": False},
]

async def processar_pedido(pedido):
    print(f'-> Processando pedido {pedido["id"]}')
    await asyncio.sleep(3)
    if pedido["pagamento_aprovado"]:
        print(f'Pagamento aprovado para pedido {pedido["id"]}.')
        if pedido['estoque_disponivel']:
            print(f'Estoque disponivel para pedido {pedido["id"]}.')
            print(f'Pedido {pedido["id"]} confirmado!\nEnviado para entrega.')
        else:
            print(f'Estoque indisponível para pedido {pedido["id"]}.\nPedido cancelado.')
    else:
        print(f'Pagamento recusado para pedido {pedido["id"]}.\nPedido cancelado.')
    print('-' * 35)
    
async def main():
    for pedido in pedidos:
        await processar_pedido(pedido)
    print('\nTodos os pedidos foram processados!')

asyncio.run(main())