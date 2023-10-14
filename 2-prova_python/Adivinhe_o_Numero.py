import random

print("\n         **** Bem vindo ****\n\nMarkin apresenta Adivinhe o número\n")

valor_A = random.randint(0,100)

while True:
  print("______________________________")
  valor_U = float(input("\nDigite o valor que quer chutar\nValor: "))
  if valor_A == valor_U:
    print("\n  ***** Você acertou *****\n\nObrigado por jogar")
    break
  elif valor_A <= valor_U:
    print(f"\nEsse numero: {valor_U} é maior que o valor secreto")
  else:
    print(f"\nEsse numero: {valor_U} é menor que o valor secreto")