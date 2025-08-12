## Criando um temporizador assíncrono

## Alice é uma desenvolvedora que precisa testar uma API de terceiros que tem um tempo de resposta variável. 
# Para simular esse comportamento, ela quer um programa que exiba uma mensagem, aguarde um tempo determinado e depois exiba outra 
## mensagem informando que o tempo acabou.
## Esse programa deve ser assíncrono, permitindo que Alice compreenda melhor como funciona a espera sem bloquear a execução do código.
##Com base nesse cenário, crie um programa que aguarde 3 segundos antes de exibir a mensagem final.

import asyncio

async def temporizador():
    print('Iniciando temporizador ...')
    await asyncio.sleep(3)
    print('Tempo finalizado após 3 segundos!!')

asyncio.run(temporizador())