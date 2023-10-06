import tkinter as tk
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
global tree
from dados import *

##cores
c1 = "#f0f3f5" #Ciza
c2 = "#feffff" #Branca
c3 = "#403d3d" #letra
c4 = "#450e63" #Roxo


## base
janela = Tk()
janela.title("Contatos Markin")
janela.geometry ("500x450")
janela.configure(background=c1)
janela.resizable(width=FALSE, height=FALSE)
style = Style(janela)
style.theme_use ("clam")


### geral
frame_cima=Frame(janela,width=500,height=50,bg=c4,relief="flat")
frame_cima.grid(row=0,column=0,pady=1,padx=0,sticky=NSEW)
frame_meio=Frame(janela,width=500,height=150,bg=c1,relief="flat")
frame_meio.grid(row=1,column=0,padx=0,sticky=NSEW)
frame_tabela=Frame(janela,width=500,height=248,bg=c2,relief="flat")
frame_tabela.grid(row=2,column=0,padx=10,columnspan=2,pady=1,sticky=NW)


## cima
titulo=Label(frame_cima,text="Agenda de Contatos",anchor=NE,font=("arial 20 bold"),bg=c4,fg=c1)
titulo.place(x=5,y=5)
linha=Label(frame_cima,text="",width=500,anchor=NE,font=("arial 1"),bg=c1,fg=c3)
linha.place(x=0,y=45)

def mostrar_dados():
  global tree
  lista = ["Nome","Numero"]
  dados = ver_dados()
  tree=ttk.Treeview(frame_tabela,selectmode="extended",columns=lista,show="headings")
  sbv=ttk.Scrollbar(frame_tabela,orient="vertical",command=tree.xview)
  sbh=ttk.Scrollbar(frame_tabela,orient="horizontal",command=tree.xview)
  tree.configure(yscrollcommand=sbv.set,xscrollcommand=sbh.set)
  tree.grid(column=0,row=0,sticky="nsew")
  sbv.grid(column=1,row=0,sticky="ns")
  sbh.grid(column=0,row=1,sticky="ew")

## tabela lista
  tree.heading(0,text="Nome",anchor=NW)
  tree.column(0,width=240,anchor="nw")
  tree.heading(1,text="Numero",anchor=NW)
  tree.column(1,width=100,anchor="nw")
  for item in dados: 
     tree.insert("","end",values=item)

mostrar_dados()
def inserir():
    nome = nome_e.get()
    numero = numero_e.get()
    dados = [ nome, numero ]
    if nome == "" or numero == "":
       messagebox.showwarning("Dados","Por favor preencher todos os campos")
    else:
       dados_add(dados)
       messagebox.showinfo("Dados","Os dados foram adicionados com sucesso")

       nome_e.delete (0,"end")
       numero_e.delete (0,"end")
       mostrar_dados()

       
def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario["values"]
        
        telefone = str(tree_lista[1])
        remover_dados(telefone)
        messagebox.showinfo("Dados","Os dados foram deletados com sucesso")
        for widget in frame_tabela.winfo_children():
              widget.destroy()
    except:
        messagebox.showwarning("Dados","Por favor selecione uma informação na tabela")
         
def procurar():
    telefone = procurar_e.get()

    dados = pesquisar_dados(telefone)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert("","end",values=item)

    procurar_e.delete(0,"end")   
## meio
nome_t=Label(frame_meio,text="Nome",anchor=NE,font=("Ivy 10 bold"),bg=c1,fg=c3)
nome_t.place(x=5,y=20)
nome_e=Entry(frame_meio,width=25,justify="left",font=("",10),highlightthickness=1)
nome_e.place(x=65,y=20)


numero_t=Label(frame_meio,text="Numero",anchor=NE,font=("Ivy 10 bold"),bg=c1,fg=c3)
numero_t.place(x=5,y=65)
numero_e=Entry(frame_meio,width=25,justify="left",font=("",10),highlightthickness=1)
numero_e.place(x=65,y=65)


procurar_t=Button(frame_meio,command=procurar,text="Procurar",font=("Ivy 8 bold"),bg=c2,fg=c3,relief=RAISED, overrelief=RIDGE)
procurar_t.place(x=265,y=19)
procurar_e=Entry(frame_meio,width=22,justify="left",font=("",10),highlightthickness=1)
procurar_e.place(x=322,y=20)

atualizar_t=Button(frame_meio,command=mostrar_dados, text="Atualizar",font=("Ivy 8 bold"),width=10,bg=c2,fg=c3,relief=RAISED, overrelief=RIDGE)
atualizar_t.place(x=265,y=49)

adicionar_t=Button(frame_meio,command=inserir, text="Adicionar",font=("Ivy 8 bold"),width=10,bg=c2,fg=c3,relief=RAISED, overrelief=RIDGE)
adicionar_t.place(x=400,y=49)

deletar_t=Button(frame_meio,command=remover ,text="Deletar",font=("Ivy 8 bold"),width=10,bg=c1,fg=c3,relief=RAISED, overrelief=RIDGE)
deletar_t.place(x=400,y=79)

janela.mainloop()

