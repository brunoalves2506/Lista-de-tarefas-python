# GERENCIADOR DE TAREFAS
import json
import os

Tarefas_Prioridade_Baixa = []
Tarefas_Prioridade_Media = []
Tarefas_Prioridade_Alta = []
Tarefas_Finalizadas = []

Cont_ID = 1

def Salvar_JSON():
    dados = {
        "Tarefas_Prioridade_Baixa": Tarefas_Prioridade_Baixa,
        "Tarefas_Prioridade_Media": Tarefas_Prioridade_Media,
        "Tarefas_Prioridade_Alta": Tarefas_Prioridade_Alta,
        "Tarefas_Finalizadas": Tarefas_Finalizadas,
        "Cont_ID": Cont_ID
    }

    with open("tarefas.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Progresso salvo com sucesso!")
    input("Pressione ENTER para continuar...")

def Carregar_JSON():
    global Cont_ID

    if not os.path.exists("tarefas.json"):
        return

    with open("tarefas.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    Tarefas_Prioridade_Baixa.extend(dados.get("Tarefas_Prioridade_Baixa", []))
    Tarefas_Prioridade_Media.extend(dados.get("Tarefas_Prioridade_Media", []))
    Tarefas_Prioridade_Alta.extend(dados.get("Tarefas_Prioridade_Alta", []))
    Tarefas_Finalizadas.extend(dados.get("Tarefas_Finalizadas", []))
    Cont_ID = dados.get("Cont_ID", 1)

def Validacao_Numero():
    entrada_ok = False
    while not entrada_ok:
        acao = input("Informe a ação a ser tomada: ")
        if acao.isdigit():
            entrada_ok = True
            return int(acao)
        else:
            print("Erro: Digite apenas números.")

def Exibir_Tarefas():
    print("==========ALTA PRIORIDADE===========")
    for tarefa in Tarefas_Prioridade_Alta:
        print(tarefa)

    print("==========MÉDIA PRIORIDADE==========")
    for tarefa in Tarefas_Prioridade_Media:
        print(tarefa)

    print("==========BAIXA PRIORIDADE==========")
    for tarefa in Tarefas_Prioridade_Baixa:
        print(tarefa)

    print("====================================")

def Exibir_Finalizadas():
    print ("===============GERENCIADOR DE TAREFAS===============")
    for tarefa in Tarefas_Finalizadas:
        print (tarefa)
        input ("Pressione ENTER para Continuar...")


def Exibir_Menu():
    print ("===============GERENCIADOR DE TAREFAS===============")
    print ("1 - EXIBIR TAREFAS ATIVAS")
    print ("2 - ADICIONAR TAREFA")
    print ("3 - EDITAR TAREFA")
    print ("4 - DAR BAIXA EM TAREFA")
    print ("5 - EXIBIR TAREFAS FINALIZADAS")
    print ("0 - FINALIZAR PROGRAMA")
    print ("====================================================")

def Adicionar_Tarefa():
    global Cont_ID

    os.system('cls')
    Nome_Tarefa = input("Informe o NOME da tarefa: ")

    print("Informe a PRIORIDADE da tarefa '1 - BAIXA / 2 - MEDIA / 3 - ALTA': ")
    prioridade_num = Validacao_Numero()

    match prioridade_num:
        case 1:
            prioridade = "BAIXA"
        case 2:
            prioridade = "MEDIA"
        case 3:
            prioridade = "ALTA"
        case _:
            print("Opção inválida. Prioridade definida como BAIXA.")
            prioridade = "BAIXA"

    print("Informe a ORIGEM da tarefa '1 - Email / 2 - Telefone / 3 - Chamado do Sistema':")
    origem_num = Validacao_Numero()

    match origem_num:
        case 1:
            origem = "Email"
        case 2:
            origem = "Telefone"
        case 3:
            origem = "Chamado do Sistema"
        case _:
            origem = "Email"

    Nova_Tarefa = {
        "ID": Cont_ID,
        "NOME": Nome_Tarefa,
        "PRIORIDADE": prioridade,
        "ORIGEM": origem,
        "STATUS": "ATIVA"
    }

    # Colocar na lista correta
    if prioridade == "ALTA":
        Tarefas_Prioridade_Alta.append(Nova_Tarefa)
    elif prioridade == "MEDIA":
        Tarefas_Prioridade_Media.append(Nova_Tarefa)
    else:
        Tarefas_Prioridade_Baixa.append(Nova_Tarefa)

    Cont_ID += 1
    print("Tarefa adicionada com sucesso!")

def Encontrar_Tarefa_ID():
    Exibir_Tarefas()

    print("Informe o ID da tarefa:")
    acao = Validacao_Numero()

    Total_Listas = [Tarefas_Prioridade_Baixa, Tarefas_Prioridade_Media, Tarefas_Prioridade_Alta]

    for lista in Total_Listas:
        for item in lista:
            if acao == item["ID"]:
                os.system('cls')
                print("==========TAREFA========")
                print(item)
                return item, lista

    print("ID não encontrado.")
    return None, None

def Editar_Tarefa():
    os.system('cls')
    print("==========EDITAR TAREFA==========")

    item, lista = Encontrar_Tarefa_ID()

    if item is None:
        input("Pressione ENTER para continuar...")
        return

    Novo_Nome = input("Informe o novo NOME da tarefa: ")

    print("Informe a nova PRIORIDADE '1 - BAIXA / 2 - MEDIA / 3 - ALTA':")
    Nova_Prioridade = Validacao_Numero()

    match Nova_Prioridade:
        case 1:
            Nova_Prioridade = "BAIXA"
        case 2:
            Nova_Prioridade = "MEDIA"
        case 3:
            Nova_Prioridade = "ALTA"

    print("Informe a nova ORIGEM '1 - Email / 2 - Telefone / 3 - Chamado do Sistema':")
    Nova_Origem = Validacao_Numero()

    match Nova_Origem:
        case 1:
            Nova_Origem = "Email"
        case 2:
            Nova_Origem = "Telefone"
        case 3:
            Nova_Origem = "Chamado do Sistema"

    # Remover da lista antiga
    lista.remove(item)

    # Atualizar os dados
    item["NOME"] = Novo_Nome
    item["PRIORIDADE"] = Nova_Prioridade
    item["ORIGEM"] = Nova_Origem

    # Inserir na lista correta
    if Nova_Prioridade == "ALTA":
        Tarefas_Prioridade_Alta.append(item)
    elif Nova_Prioridade == "MEDIA":
        Tarefas_Prioridade_Media.append(item)
    else:
        Tarefas_Prioridade_Baixa.append(item)

    print("==========TAREFA EDITADA========")
    print(item)
    input("Pressione ENTER para continuar...")

def Baixa_Tarefa():
    item, lista = Encontrar_Tarefa_ID()
    item["STATUS"] = "FINALIZADA"

    if item is None:
        input("Pressione ENTER para continuar...")
        return

    lista.remove(item)
    Tarefas_Finalizadas.append(item)

    print("Tarefa finalizada com sucesso!")
    input("Pressione ENTER para continuar...")

# ============ LOOP PRINCIPAL =============

Carregar_JSON()

while True:
    os.system('cls')
    Exibir_Menu()
    acao = Validacao_Numero()

    match acao:

        case 1:
            os.system('cls')
            print("==========LISTA DE TAREFAS==========")
            Exibir_Tarefas()
            input("Pressione ENTER para continuar...")

        case 2:
            Adicionar_Tarefa()

        case 3:
            Editar_Tarefa()

        case 4:
            os.system('cls')
            print("===============DAR BAIXA EM TAREFA===============")
            Baixa_Tarefa()

        case 5:
            os.system('cls')
            Exibir_Finalizadas()

        case 0:
            Salvar_JSON()
            break
