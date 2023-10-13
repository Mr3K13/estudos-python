print("\n *********** Bem Vindos ***********")
print("\nObrigado por escolher a casa de câmbio Markin\n\nEsses valores são ipoteticos")
def menu():
   menu_v = int(input("\nQual moeda o Sr.(a) deseja ?\n1 - REAL \n2 - DOLLAR \n3 - EURO\n4 - KWANZA\n\nOpção: "))
   print("______________________________")
   if menu_v == 1:
      menu_v2 = int(input("\nA primeira moeda selecionada foi: REAL\n\nPorfavor escolha para qual vai converter:\n1 - DOLLAR \n2 - EURO\n3 - KWANZA\n\nOpção: "))
      print("______________________________")
      if menu_v2 == 1:
         valor = float(input("\nA primeira foi: REAL\nA segunda foi:  DOLLAR\n\nQuantos Reais quer converte em Dolares?\n\nValor: R$"))
         print("______________________________")
         valor_f = valor * 0.20
         print(f"\nO seu valor foi: ${valor_f}\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 2 :
         valor = float(input("\nA primeira foi: REAL\nA segunda foi:  EURO\n\nQuantos Reais quer converte em Euros?\n\nValor: R$"))
         print("______________________________")
         valor_f = valor * 0.19
         print(f"\nO seu valor foi: {valor_f} €\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 3:
         valor = float(input("\nA primeira foi: REAL\nA segunda foi:  KUANZA\n\nQuantos Reais quer converte em Kuanzas?\n\nValor: R$"))
         print("______________________________")
         valor_f = valor * 162.51
         print(f"\nO seu valor foi: {valor_f} Kz\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
   elif menu_v == 2:
      menu_v2 = int(input("\nA primeira moeda selecionada foi: DOLLAR\n\nPorfavor escolha para qual vai converter:\n1 - REAL \n2 - EURO\n3 - KWANZA\n\nOpção: "))
      print("______________________________")
      if menu_v2 == 1:
         valor = float(input("\nA primeira foi: DOLLAR\nA segunda foi:  REAL\n\nQuantos Dolares quer converte em Reais?\n\nValor: $"))
         print("______________________________")
         valor_f = valor * 5.08
         print(f"\nO seu valor foi: R${valor_f}\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 2 :
         valor = float(input("\nA primeira foi: DOLLAR\nA segunda foi:  EURO\n\nQuantos Dolares quer converte em Euros?\n\nValor: $"))
         print("______________________________")
         valor_f = valor * 0.95
         print(f"\nO seu valor foi: {valor_f} €\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 3:
         valor = float(input("\nA primeira foi: DOLLAR\nA segunda foi:  KUANZA\n\nQuantos Dolares quer converte em Kuanzas?\n\nValor: $"))
         print("______________________________")
         valor_f = valor * 825.53
         print(f"\nO seu valor foi: {valor_f} Kz\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
   elif menu_v == 3:
      menu_v2 = int(input("\nA primeira moeda selecionada foi: EURO\n\nPorfavor escolha para qual vai converter:\n1 - REAL \n2 - DOLLAR\n3 - KWANZA\n\nOpção: "))
      print("______________________________")
      if menu_v2 == 1:
         valor = float(input("\nA primeira foi: EURO\nA segunda foi:  REAL\n\nQuantos Euros quer converte em Reais?\n\nValor: "))
         print("______________________________")
         valor_f = valor * 5.34
         print(f"\nO seu valor foi: R${valor_f}\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 2 :
         valor = float(input("\nA primeira foi: EURO\nA segunda foi:  EURO\n\nQuantos Euros quer converte em Dolares?\n\nValor: "))
         print("______________________________")
         valor_f = valor * 1.05
         print(f"\nO seu valor foi: ${valor_f}\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 3:
         valor = float(input("\nA primeira foi: EURO\nA segunda foi:  KUANZA\n\nQuantos Euros quer converte em Kuanzas?\n\nValor: "))
         print("______________________________")
         valor_f = valor * 867.83
         print(f"\nO seu valor foi: {valor_f} Kz\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
   elif menu_v == 4:
      menu_v2 = int(input("\nA primeira moeda selecionada foi: KWANZA\n\nPorfavor escolha para qual vai converter:\n1 - REAL \n2 - DOLLAR\n3 - KWANZA\n\nOpção: "))
      print("______________________________")
      if menu_v2 == 1:
         valor = float(input("\nA primeira foi: KWANZA\nA segunda foi:  REAL\n\nQuantas Kuanzas quer converte em Reais?\n\nValor: "))
         print("______________________________")
         valor_f = valor / 162.51
         print(f"\nO seu valor foi: R${valor_f}\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 2 :
         valor = float(input("\nA primeira foi: KWANZA\nA segunda foi:  DOLLAR\n\nQuantas Kuanzas quer converte em Dolares?\n\nValor: "))
         print("______________________________")
         valor_f = valor / 825.53
         print(f"\nO seu valor foi: ${valor_f}\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
      elif menu_v2 == 3:
         valor = float(input("\nA primeira foi: KWANZA\nA segunda foi:  EURO\n\nQuantas Kuanzas quer converte em Euros?\n\nValor: "))
         print("______________________________")
         valor_f = valor / 867.83
         print(f"\nO seu valor foi: {valor_f} €\n\nObrigado por escolher a casa de câmbio Markin\n\n*********** Até uma proxima ***********\n")
menu()