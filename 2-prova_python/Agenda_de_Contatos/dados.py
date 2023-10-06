import csv
def dados_add(i):  
 with open("C:/Users/ph154/OneDrive/Documentos/GitHub/estudos-python/2-prova_python/Agenda_de_Contatos/dados.csv","a+",newline="")as file:
   escrever=csv.writer(file)
   escrever.writerow(i)

def ver_dados():
  dados=[]
  with open("C:/Users/ph154/OneDrive/Documentos/GitHub/estudos-python/2-prova_python/Agenda_de_Contatos/dados.csv") as file:
    ler_csv = csv.reader(file)
    for linha in ler_csv:
     dados.append(linha)
  return dados
def remover_dados(i):

  def adicionar_novalista(j):  
     with open("C:/Users/ph154/OneDrive/Documentos/GitHub/estudos-python/2-prova_python/Agenda_de_Contatos/dados.csv","w",newline="")as file:
         escrever=csv.writer(file)
         escrever.writerows(j)
         ver_dados()

  nova_lista=[]
  telefone= i
  with open("C:/Users/ph154/OneDrive/Documentos/GitHub/estudos-python/2-prova_python/Agenda_de_Contatos/dados.csv","r")as file:
      ler_csv=csv.reader(file)

      for linha in ler_csv:
          nova_lista.append(linha)
          for campo in linha:
              if campo == telefone:
                 nova_lista.remove(linha)

  adicionar_novalista(nova_lista)

def pesquisar_dados(i):
  dados = []
  telefone = i
 
 
  with open("C:/Users/ph154/OneDrive/Documentos/GitHub/estudos-python/2-prova_python/Agenda_de_Contatos/dados.csv") as file:
       ler_csv= csv.reader(file)
       for linha in ler_csv:
           for campo in linha:
               if campo == telefone:
                  dados.append(linha)
  return dados
