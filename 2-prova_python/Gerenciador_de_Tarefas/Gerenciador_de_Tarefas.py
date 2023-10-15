import json
print("\n *********** Bem-vindos ***********")
print("\nObrigado por escolher o Gerenciador Markin\n")
def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
    return tarefas

def salvar_tarefas(tarefas):
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo, indent=2)

def listar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas.")
    else:
        for i, tarefa in enumerate(tarefas, start=1):
            concluida = "✔" if tarefa["concluida"] else " "
            print(f"{i}. [{concluida}] {tarefa['descricao']}")

def adicionar_tarefa(tarefas, descricao):
    tarefas.append({'descricao': descricao, 'concluida': False})
    salvar_tarefas(tarefas)
    print(f"Tarefa '{descricao}' adicionada com sucesso!")

def marcar_como_concluida(tarefas, numero):
    if 1 <= numero <= len(tarefas):
        tarefas[numero - 1]['concluida'] = True
        salvar_tarefas(tarefas)
        print(f"Tarefa {numero} marcada como concluída.")
    else:
        print("Número de tarefa inválido.")

def remover_tarefa(tarefas, numero):
    if 1 <= numero <= len(tarefas):
        tarefa_removida = tarefas.pop(numero - 1)
        salvar_tarefas(tarefas)
        print(f"Tarefa '{tarefa_removida['descricao']}' removida com sucesso.")
    else:
        print("Número de tarefa inválido.")

def main():
    tarefas = carregar_tarefas()
    
    while True:
        print("\n===== Aplicativo de Gerenciamento de Tarefas =====")
        print("1. Listar Tarefas")
        print("2. Adicionar Tarefa")
        print("3. Marcar Tarefa como Concluída")
        print("4. Remover Tarefa")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            listar_tarefas(tarefas)
        elif opcao == '2':
            descricao = input("Digite a descrição da tarefa: ")
            adicionar_tarefa(tarefas, descricao)
        elif opcao == '3':
            listar_tarefas(tarefas)
            numero = int(input("Digite o número da tarefa concluída: "))
            marcar_como_concluida(tarefas, numero)
        elif opcao == '4':
            listar_tarefas(tarefas)
            numero = int(input("Digite o número da tarefa a ser removida: "))
            remover_tarefa(tarefas, numero)
        elif opcao == '0':
            
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()