import time

#narrativa inicial:
def run_case4():
    print("Iniciando investigação do caso 4...")
    time.sleep(3)

    print("Uma escola relatou problemas no sistema de cadastro de alunos...")
    time.sleep(3)

    print("Ao atualizar as informações de um aluno, os demais registros deveriam permanecer salvos...")
    time.sleep(3)

    print("No entanto, após algumas atualizações, alunos que estavam cadastrados desaparecem da lista sem explicação...")
    time.sleep(3)

    print("Sua missão é investigar o código e descobrir por que os registros estão sendo perdidos.")
    time.sleep(4)

#código bugado
    codigo_bugado4 = """Código Bugado para análise:


    lista_de_alunos = ["Maria", "João", "Ana"]

    def atualizar_aluno(nome, novo_nome):

        # Atualizar cadastro da Maria

        lista_de_alunos = ["Maria Silva"]

    atualizar_aluno("Maria", "Maria Silva")


    """

#output/comportamento observado 
    output = """ Lista de alunos antes da atualização:
    ["Maria", "João", "Ana"]

    Lista de alunos após a atualização:
    ["Maria Silva"]
    """
    print(codigo_bugado4)
    time.sleep(2)
    print(output)
    time.sleep(3)

#investigações
    menu_case4 = """ Menu de Pistas:
    1. Verificar quantidade de alunos cadastrados
    2. Analisar lista após a atualização
    """ 
#diagnóstico
    investigacao = 0
    while investigacao < 2:
        print(menu_case4)
        escolha = input("Escolha uma opção para investigar: ")  
        if escolha == "1":
            print("Antes da atualização existiam 3 alunos cadastrados. Após a atualização, apenas 1 permaneceu na lista.")
            investigacao += 1
        elif escolha == "2":
            print("Após a atualização, a lista contém apenas o registro atualizado da Maria.")
            investigacao += 1
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")



#resultado final

    menu_decisao_final4 = """
    1. A lista de alunos foi substituída por uma nova lista durante a atualização.
    2. O sistema remove alunos antigos automaticamente após uma atualização.
    """

    print(menu_decisao_final4)


    decisao_final4 = input("Qual é a causa do bug? ")
    if decisao_final4 == "1":
        print("Correto! Durante a atualização, a lista original de alunos foi substituída por uma nova lista contendo apenas o registro atualizado. Como os demais alunos não foram preservados, seus cadastros foram perdidos.")
        return True
        
    elif decisao_final4 == "2":
        print("Incorreto! O problema não está em uma remoção automática de alunos. A lista original foi substituída durante a atualização, causando a perda dos demais registros.")
        return False
    else:   
        print("Opção inválida. Por favor, escolha uma opção válida.")
        return False