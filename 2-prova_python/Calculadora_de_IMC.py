print("\n         **** Bem vindo ****\n\nMarkin apresenta Calculadora de IMC\n")
print("______________________________")
peso = float(input("\nPorfavor inserir o peso: "))
altura = float(input("\nPorfavor inserir a altura: "))
imc = peso / (altura**2)
print("______________________________")
print(f"\nO IMC é de: {imc:.2f}\n")

if imc < 18.5:
    print("Você está abaixo do peso ideal.")
elif 18.5 <= imc < 24.9:
    print("Seu peso está na faixa saudável.")
elif 24.9 <= imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")
print("______________________________")
print("\n\nObrigado por usar mais um código Markin\n\n*********** Até uma próxima ***********\n")
