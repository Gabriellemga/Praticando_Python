## Gerenciando inscrições em cursos

#Paula trabalha em uma plataforma de ensino online e precisa garantir que os alunos sejam inscritos corretamente nos cursos desejados. 
# O sistema deve seguir as seguintes regras:

#Cada aluno pode se inscrever em um curso, mas antes a plataforma precisa verificar se há vagas disponíveis;
#Se houver vagas, o aluno deve ser confirmado na turma e a vaga deve ser reduzida;
#Se não houver vagas, o aluno deve ser notificado de que a turma está lotada;
#Se um aluno já estiver inscrito, ele não pode se inscrever novamente no mesmo curso.

# A lista de alunos e os cursos disponíveis já está definida no sistema. 
# Lembre-se de processar múltiplas inscrições em paralelo.

import asyncio

cursos = {
    "Python Avançado": {"vagas": 2, "inscritos": []},
    "Java para Iniciantes": {"vagas": 1, "inscritos": []},
    "Machine Learning": {"vagas": 0, "inscritos": []},
}

alunos = [
    {"nome": "Alice", "curso": "Python Avançado"},
    {"nome": "Bruno", "curso": "Python Avançado"},
    {"nome": "Carlos", "curso": "Java para Iniciantes"},
    {"nome": "Daniela", "curso": "Machine Learning"},
    {"nome": "Alice", "curso": "Python Avançado"},  # Tentativa de inscrição duplicada
]

lock = asyncio.Lock()

async def inscrever(aluno):
    nome = aluno["nome"]
    curso = aluno["curso"]

    print(f"\nInscrevendo {nome} no curso {curso}...")

    async with lock:
        dados_curso = cursos.get(curso)

        if nome in dados_curso["inscritos"]:
            print(f"{nome} já está inscrita no curso {curso}! Inscrição rejeitada.")
            return

        if dados_curso["vagas"] > 0:
            dados_curso["inscritos"].append(nome)
            dados_curso["vagas"] -= 1
            print(f"Inscrição confirmada para {nome} no curso {curso}!")
        else:
            print(f"Turma lotada! {nome} não pôde se inscrever no curso {curso}.")

    await asyncio.sleep(1)

async def main():
    tarefas = [asyncio.create_task(inscrever(aluno)) for aluno in alunos]
    await asyncio.gather(*tarefas)

    print("\nTodas as inscrições foram processadas!")

asyncio.run(main())
        

        


