print("\n         **** Bem vindo ****\n\nMarkin apresenta calculadora de notas")
num_notas = int(input("\nQuantas notas deseja inserir? "))
soma_notas = 0
for i in range(num_notas):
    nota = float(input(f"\nInsira a nota {i + 1}: "))
    soma_notas += nota
media_notas = soma_notas / num_notas
def calcular_nota(media):
    if media >= 10:
        return "A"
    elif media >= 9:
        return "B"
    elif media >= 8:
        return "C"
    elif media >= 7:
        return "D"
    else:
        return "F"
media_final = calcular_nota(media_notas)
print("\nA média das notas é: ",media_notas)
print("\nA nota correspondente é: ",media_final)