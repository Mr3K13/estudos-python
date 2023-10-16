import random
print("\n *********** Bem Vindos ***********")
print("\nObrigado por escolher a forca Markin")
letras_tentativas = []
chances = 5
ganhou = False
with open("palavras.txt", "r") as arquivo:
    palavras = arquivo.read().splitlines()
palavra = random.choice(palavras)


while True:
    acertos = 0
    print("")
    for letra in palavra:
        if letra.lower() in letras_tentativas:
            print(letra, end=" ")
            acertos += 1

        else:
            print("_", end=" ")

    if acertos == len(palavra):
        ganhou = True
        break

    tentativa = input("\nChute uma letra: ")

    letras_tentativas.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    if chances == 0:
        break

if ganhou:
    print(f"\n\nParabéns! Você ganhou.\n\nA palavra era {palavra}\n")
    print("\n\nObrigado por usar mais um código Markin\n\n*********** Até uma próxima ***********\n")
else:
    print(f"\nVocê perdeu.\n\nA palavra era {palavra}\n")
    print("\n\nObrigado por usar mais um código Markin\n\n*********** Até uma próxima ***********\n")
