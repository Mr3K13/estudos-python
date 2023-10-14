import time
print("\n *********** Bem Vindos ***********")
print("\nObrigado por escolher o banco Markin")
valor = 1000

def menu(valor):
   menu_v = int(input("\nO que o Sr.(a) deseja ? \n1 - Sacar\n2 - Depositar\n3 - Extrato\n0 - Sair\n\nOpção: "))
   print("______________________________")
   if menu_v == 1:
     print("\nO Sr(a) escolheu a opiçao de Saque")
     time.sleep(0.7)
     saque = float(input("\nQual valor o Sr.(a) deseja sacar? "))
     valor -= saque
     time.sleep(0.7)
     print(f"\nNovo saldo: R${valor}")
     time.sleep(0.7)
     menu(valor)

   elif menu_v == 2:
      print("\nO Sr(a) escolheu a opiçao de Deposito")
      time.sleep(0.7)
      deposito = float(input("\nQual valor o Sr.(a) depositar? "))
      valor += deposito
      time.sleep(0.7)
      print(f"\nNovo saldo: R${valor}")
      time.sleep(0.7)
      menu(valor)

   elif menu_v == 3:
      print(f"\nO Sr(a) escolheu a opição Extrato\n\nO valor atual na sua conta é de: R${valor}")
      time.sleep(1)
      menu(valor)
      
   elif menu_v == 0:
      print(f"\n brigado por escolher o banco Markin\n\nO seu saldo final foi: R${valor}\n\n*********** Até uma proxima ***********\n")
   
   else:
      print("\nO Sr(a) inseriu um valor incorreto. Por favor, insira um valor válido.")
      time.sleep(0.7)
      menu(valor)
      
menu(valor)