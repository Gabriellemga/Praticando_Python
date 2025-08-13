## Validando um CPF

#Carlos trabalha em um cartório e precisa validar se um CPF informado pelo cliente tem o formato correto antes de 
# prosseguir com o atendimento. O CPF deve conter exatamente 11 dígitos numéricos. Se a entrada contiver letras ou 
# qualquer outro caractere que não seja um número, o programa deve exibir uma mensagem de erro.Crie um programa que 
# peça ao usuário um número de CPF e verifique se ele tem 11 dígitos e contém apenas números.


import re


cpf = input("Digite o número do cpf: ")


tem_letras = re.search(r"[a-zA-Z]", cpf)
tem_caracteres_especiais = re.search(r"[\'\",.!:;#@\-\s]", cpf)
numero_digitos = 11


if len(cpf) != 11: 
    print("O CPF deve conter 11 digitos.")
    if tem_letras:
        print("O cpf não deve conter letra.")
        if tem_caracteres_especiais:
            print("O cpf não deve ter caracteres especiais.")
else:
    print("O CPF  é válido.")
