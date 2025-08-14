##Gerenciador de tarefas

#Ana precisa de um programa simples para gerenciar suas tarefas diárias. Ela quer poder adicionar, visualizar 
#e remover tarefas de uma lista.
#Crie um programa com um menu interativo que permita ao usuário adicionar, visualizar e remover tarefas. 

#Use uma lista para armazenar as tarefas.

def adicionar_tarefa(tarefas):
  tarefa_add = input('Digite a tarefa:')
  tarefas.append(tarefa_add)
  print('Tarefa adicioda !')
  return 

def visualizar_tarefa(tarefas):
  print('Tarefas :')
  for i in range(len(tarefas)):
    print(f'{i +1}.{tarefas[i]} ')
  return
  
def remover_tarefa(tarefas):
  visualizar_tarefa(tarefas)
  tarefa_remover = int(input('Digite o número da tarefa a ser removida: ')) - 1
  tarefas.pop(tarefa_remover)
  print(f'Tarefa {tarefas[tarefa_remover]} removida')
  return

def gerenciar_tarefas():
  tarefas = []
  while True:
    try:
      print('''Escolha uma das opções disponiveis\n
      1. Adicionar tarefa 
      2. Visualizar tarefas 
      3. Remover tarefa 
      4. Sair 
      ''')
      opcao = int(input('-> '))
      if opcao == 1:
        adicionar_tarefa(tarefas)
      elif opcao == 2:
        visualizar_tarefa(tarefas)
      elif opcao == 3:
        remover_tarefa(tarefas)
      elif opcao == 4:
        print('Saindo do gerenciador de tarefas. Até mais!')
        break
      else:
        print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')
    except ValueError:
      print("Erro: Entrada inválida. Digite um número.")

gerenciar_tarefas()
