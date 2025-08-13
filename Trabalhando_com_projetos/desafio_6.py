## Pedra, papel e tesoura

#Ele precisa de um programa que permita ao usuário escolher uma opção e depois exiba o resultado da partida.

#Crie um programa que permita ao usuário escolher entre pedra, papel ou tesoura. O computador escolherá aleatoriamente uma opção. O programa deve exibir quem venceu a partida. Lembrando que:

#Pedra ganha de Tesoura (Pedra quebra Tesoura);
#Tesoura ganha de Papel (Tesoura corta Papel);
#Papel ganha de Pedra (Papel cobre Pedra);
#Se ambos escolherem a mesma opção, é um empate.

import random

print("Escolha seu movimento (Pedra, Papel or Tesoura)\n")
jogador = input("Jogador -> ").lower()
computador = random.choices(["pedra","papel", "tesoura"])

if jogador == computador:
  print("\n Empate! 😉")
elif jogador == "pedra":
  if computador == "tesoura":
    print("\n A pedra ⛰️ jogador quebra a tesoura ✂️ do computador.")
  else:
    print("\n O papel 📄 do computador cobre a pedra ⛰️ do jogador.")
elif jogador == "papel":
  if computador == "pedra":
    print("\n O papel 📄 do jogador cobre a  pedra ⛰️ do computador.")
  else:
    print("\ A tesoura ✂️ do computador corta o papel 📄 do jogador.")
elif jogador == "tesoura":
  if computador == "papel":
    print("\n A  tesoura ✂️ do jogador corta o papel 📄 do computador.")
  else:
    print("\nA pedra ⛰️ do computador quebra a tesoura ✂️ do jogador")