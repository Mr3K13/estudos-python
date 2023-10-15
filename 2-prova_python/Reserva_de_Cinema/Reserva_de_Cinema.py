import csv
global tree

## Inicio

print("\n *********** Bem-vindos ***********")
print("\nObrigado por escolher o Cine Markin\n")
print("______________________________")

## Função
def inserir(filme_v,horario_v):
    print("______________________________")
    nome = input("\nDigite o seu nome: ")
    filme = filme_v
    horario = horario_v
    dados = [ nome, filme, horario ]
    if nome == "":
       print("\nPor favor preencher seu nome.")
       
       inserir(filme_v,horario_v)
    else:
       dados_add(dados)
       print("\nA sua reserva foi concluida")
       print("______________________________")
       print("\nObrigado por escolher o Cine Markin\n\n*********** Até uma proxima ***********\n")

def dados_add(i):  
 with open("Reservas.csv","a+",newline="")as file:
   escrever=csv.writer(file)
   escrever.writerow(i)

def ver_dados():
  dados=[]
  with open("Reservas.csv") as file:
    ler_csv = csv.reader(file)
    for linha in ler_csv:
     dados.append(linha)
     print(linha)
  print("\n\n\n")   


## Interação

def horarios(filme_v) :
  menu_2 = int(input("\nEscolha o horario:\n\n1 - 13h\n2 - 15h\n3 - 17h\n\nOpição: "))
  print("______________________________\n")
  if menu_2   == 1:
    horario_v = "13h"
  elif menu_2 == 2:
    horario_v = "15h"
  elif menu_2 == 3:
    horario_v = "17h"
  else :
    print("Porfavor colocar um valor valido.")
    print("______________________________")
    horarios(filme_v)
  print(f"\nO Horio escolhido foi: {horario_v}")
  verificador = int(input("\n  Valide a escolha\n\n1 - SIM     2 - NÃo\n\nOpição: "))
  if verificador == 1:
    inserir(filme_v,horario_v)

  elif verificador == 2:
     print("______________________________")
     horarios(filme_v)
  else :
    print("\n______________________________")
    print("\nPorfavor colocar um valor valido.")
    print("______________________________")
    horarios(filme_v)
def menufilmes():

 print("\nEstes são os filmes tem cartaz:")
 menu_v = int(input("\n\n1 - Minecraft o Filme\n2 - Os Vingadores 73\n3 - Samara\n4 - Capitão Angola\n\nOpição: "))
 print("______________________________\n")
 if menu_v   == 1:
    filme_v = "Minecraft o Filme"
 elif menu_v == 2:
    filme_v = "Os Vingadores 73"
 elif menu_v == 3:
    filme_v = "Samara"
 elif menu_v == 4:
    filme_v = "Capitão Angola"
 elif menu_v == 666:
    ver_dados()
    
 else :
    print("Porfavor colocar um valor valido.")
    print("______________________________")
    menufilmes()
 print(f"O filme escolhido foi: {filme_v}")
 verificador = int(input("\n  Valide a escolha\n\n1 - SIM     2 - NÃo\n\nOpição: "))
 if verificador == 1:
    print("______________________________")
    horarios(filme_v)

 elif verificador == 2:
     print("______________________________")
     menufilmes()
 else:
    print("______________________________")
    print("\nPorfavor colocar um valor valido.")
    print("______________________________")
    menufilmes()
menufilmes()