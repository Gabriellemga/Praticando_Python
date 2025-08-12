## Sistema de notificação inteligente

#Lucas trabalha em um sistema de notificações que precisa enviar mensagens para usuários. 
# No entanto, algumas notificações só devem ser enviadas se o usuário tiver ativado essa opção no sistema. 
# Além disso, se o usuário for VIP, ele deve receber uma notificação prioritária antes das demais.
# Com base nesse cenário, crie um programa que simule o envio de notificações para três usuários. 
# Cada usuário tem um status diferente:

# Ana: VIP (deve receber uma notificação prioritária antes das normais).
# João: Usuário comum, mas ativou as notificações.
# Carla: Usuária comum, mas desativou as notificações (não deve receber nada).
# O programa deve exibir quais notificações foram enviadas e quais usuários não receberam nada.

import asyncio

clientes = [
    {'nome': 'Ana', 'vip': True, 'notificação': False},
    {'nome': 'João', 'vip': False, 'notificação': True},
    {'nome': 'Carla', 'vip': False, 'notificação': False},
]

async def notificacoes(cliente):
    await asyncio.sleep(3)
    if cliente['vip']:
        print(f'Notificação VIP para {cliente['nome']} enviada!')
    elif cliente['notificação']:
        print(f'Notificação normal para {cliente['nome']} enviada!')
    else:
        print(f'{cliente['nome']} desativou as notificações. Nada foi enviado.')
    

async def main():
    print('Enviando notificações...\n')
    tarefas = [asyncio.create_task(notificacoes(cliente)) for cliente in clientes]
    await asyncio.gather(*tarefas)
    print('Todas as notificações foram enviadas')


asyncio.run(main())